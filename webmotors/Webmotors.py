import pickle
import pandas as pd
import numpy as np
import math

class Webmotors(object):
    
    def __init__(self):
        
        self.Robust_scaler = pickle.load(open('Models/Robust_scaler.pkl','rb'))
    
    def atributo_frequencia(self, atributo):
        atributo_dict = atributo.value_counts().to_dict()
        df_atributo_dict = pd.DataFrame(atributo_dict.items(), columns=['Value', 'Count'])
        df_atributo_dict['frequency'] = df_atributo_dict['Count'] / df_atributo_dict['Count'].sum()
        atributo_frequencia = df_atributo_dict.set_index('Value').to_dict()['frequency']
        return atributo_frequencia

    def frequencias_codificadas(self, data_frame, freq_dict=None):
        freq_codificada = pd.DataFrame()
        for column in data_frame.columns:
            if freq_dict is not None and column in freq_dict:
                freq_codificada[column] = data_frame[column].map(freq_dict[column]).astype(float).fillna(0)
            else:
                freq_codificada[column] = data_frame[column].map(self.atributo_frequencia(data_frame[column])).astype(float).fillna(0)
        return freq_codificada
    

    
    def data_preparation(self, df1):
        frequencia = "Models/freq_dict.pkl"
        with open(frequencia, "rb") as arquivo:
            freq_dict_ = pickle.load(arquivo)
            
        df1['leads'] = df1['leads'].astype( float )
        df1['views'] = df1['views'].astype( float )
        df1['cliques_telefone'] = df1['cliques_telefone'].astype( float )
        df1['qtd_fotos'] = df1['qtd_fotos'].astype( float )
        df1['vlr_mercado'] = df1['vlr_mercado'].astype( float )
        df1['vlr_anuncio'] = df1['vlr_anuncio'].astype( float )
        df1['km_veiculo'] = df1['km_veiculo'].astype( int )
        df1['cod_modelo_veiculo'] = df1['cod_modelo_veiculo'].astype( str )
        df1['ano_modelo'] = df1['ano_modelo'].astype( int )
        df1['cep_2dig'] = df1['cep_2dig'].astype( str )
        df1['cidade'] = df1['cidade'].astype( str ) 
        df1['cod_tipo_pessoa'] = df1['cod_tipo_pessoa'].astype( str )
        
        df1[['leads', 'views', 'cliques_telefone', 'vlr_anuncio', 'qtd_fotos', 'km_veiculo',
             'vlr_mercado']] = self.Robust_scaler.transform(df1[['leads', 'views', 'cliques_telefone', 
                                                                 'vlr_anuncio', 'qtd_fotos', 'km_veiculo',
                                                                 'vlr_mercado']])   
        
        df1[['cod_modelo_veiculo', 'ano_modelo', 'cep_2dig',
             'cidade', 'cod_tipo_pessoa']] = self.frequencias_codificadas(df1[['cod_modelo_veiculo',
                                                                               'ano_modelo', 'cep_2dig',
                                                                               'cidade', 'cod_tipo_pessoa']], freq_dict_)
        
        df1 = df1.astype(float)
        df1.drop(columns=['vlr_anuncio'], inplace = True)
        df1 = df1[['qtd_fotos','leads','cliques_telefone','cod_tipo_pessoa','vlr_mercado','views','cidade',
           'km_veiculo','cep_2dig','ano_modelo','cod_modelo_veiculo']]

        return df1
    
    def get_prediction( self, model, original_data, test_data ):
        
        # predição
        pred = model.predict( test_data )
        original_data['predicao'] = pred 

        for idx, _ in original_data.iterrows():
            if (original_data['predicao'].at[idx]==0):
                original_data['predicao'].at[idx]='Ideal'
            elif (original_data['predicao'].at[idx]==2):
                original_data['predicao'].at[idx]='Quase_ideal'
            elif (original_data['predicao'].at[idx]==1):
                original_data['predicao'].at[idx]='Normal'
            else:
                original_data['predicao'].at[idx]='Desqualificado'
        
        return original_data.to_json( orient='records', date_format='iso' ) 
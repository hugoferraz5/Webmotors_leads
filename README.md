# Webmotors_leads
Projeto com o objetivo de melhorar o desempenho dos anúncios para potencializar o recebimento de leads.

<div align="center">
<img src="https://user-images.githubusercontent.com/91911052/180570055-64d32e4f-9123-4afa-a84b-6ab0cc5091ba.jpg" width="700px" />
</div>

## 1 O que é a Webmotors e a venda online de veículos?
* A Webmotors foi criada em 1995 e foi a primeira startup brasileira de abrangência nacional a oferecer uma forma de comprar e vender carros e motos totalmente on-line.
Sendo o primeiro catálogo e classificado on-line automobilístico brasileiro, definição inicial da Webmotors, a empresa foi idealizada por Sylvio de Barros e desenvolvida com Marcelo Zamprogna Krug e a Team Systems, empresa de soluções para internet no Brasil.
* Os dados mostram que 2021, a venda online em todas as plataformas de vendas somadas tiveram um aumento de apenas 3% na venda de carros em relação ao ano anterior, 2020, totalizando 2,120 milhões de unidades no país.
* Com a consolidação dos meios digitais como aliados em nossas vidas, nada mais habitual do que utilizar novas ferramentas e recursos para comprar e vender carros pela internet, afinal, a instantaneidade e a comodidade são praticamente requisitos para quem deseja facilidade para negociar.

# 2 Apresentação
Nesse projeto, propus um modelo de classificação com o objetivo de predizer se alguns anúncios são capazes de obterem leads ou não.Um
lead é uma demonstração de interesse de um comprador para um vendedor. A fim de melhorar o desempenho dos anúncios, obtivemos ótimos resultados. Algumas informações foram coletadas neste link:
<a href="https://www.webmotors.com.br/wm1/dinheiro-e-economia/webmotors-revoluciona-compra-venda#:~:text=A%20Webmotors%20cobra%201%2C5,um%20custeando%200%2C75%25.">siteWebmotors</a>

O projeto completo pode ser encontrado neste link:
<a href="https://github.com/hugoferraz5/Webmotors_leads/blob/main/Classifica%C3%A7%C3%A3o_webmotors.ipynb">Webmotors</a>

|Atributo | Definição
------------ | -------------
|cod_anuncio	|código do anúncio
|	cod_cliente	|código do anunciante
|	cod_tipo_pessoa	|tipo de anunciante: PF=1, PJ=2
|	prioridade	|prioridade do anúncio (1=alta, 2-média, 3-baixa)
|	leads|	tota de propostas recebidas
| views|	quantidade de visualizações no anúncio
|	cliques_telefone|	quantidade de cliques no telefone anunciado
|	cod_marca_veiculo	|código da marca do veículo
|	cod_modelo_veiculo|	código do modelo veículo
|	cod_versao_veiculo|	código da versão do veículo
|	ano_modelo|	ano-modelo do veículo
|	cep_2dig|	dois primeiros dígitos do cep do anunciante
|	uf_cidade|	UF e cidade do anunciante
|	vlr_anuncio|	valor do veículo no anúncio
|	qtd_fotos|	quantidade de fotos no anúncio
|	km_veiculo|	Kilometragem do veículo
|	vlr_mercado	|valor de referência do veículo na praça
|	flg_unico_dono	|indicador de único dono
|	flg_licenciado	|indicador de licenciamento em dia
|	flg_ipva_pago|	indicador de IPVA em dia
|	flg_todas_revisoes_concessionaria	|indicador realização de todas as revisões na c...
|	flg_todas_revisoes_agenda_veiculo	|indicador realização de todas as revisões prev...
|	flg_garantia_fabrica|	indicador de veículo em garantia de fábrica
|	flg_blindado|	indicador de blindagem
|	flg_aceita_troca|	indicador de que o anunciante aceita troca
|	flg_adaptado_pcd|	indicador de veículo adaptado para pessoa com ...
|	combustivel	|especificação de combustível
|	cambio|	especificação de câmbio
|	portas|	número de portas
|	alarme|	presença de alarme
|	airbag|	presença de airbag
|	arquente|	presença de ar quente
|	bancocouro	|presença de banco de couro
|	arcondic	|presença de ar condicionado
|	abs|	presença de freio abs
|	desembtras|	presença de desembaçador traseiro
|	travaeletr|	presença de travas elétricas
|	vidroseletr|	presença de vidros elétricos
|	rodasliga|	presença de rodas de liga-leve
|	sensorchuva|	presença de sensor de chuva
|	sensorestacion	|presença de sensor de estacionamento

# 3 Premissas de negócio
* O histórico de automóveis com recorde de quilometragem foi essencial para análise de detecção
* O histórico de valores de anúncios foi importante na análise de preços
* Os gráficos ajudaram a ter mais clareza nas análises
* O valor de mercado foi deixado com várias casas decimais para não perder informações
* O histórico de cada anúncio ajudou nas conclusões

# 4 Passo a passo da solução

* **Questão de Negócios** - Fazer a predição de futuros anúncios da Webmotors e descobrir de forma rápida se possui leads ou não, com o objetivo de aumentar seu lucro.
* **Entendimento do negócio** - Entender o histórico dos anúncios através dos dados disponibilizados. A partir desses dados, fazer as análises.
* **Coleta de Dados** - Coletar os dados fictícios da empresa
* **Limpeza dos Dados** - Fazer a limpeza dos dados se existirem valores discrepantes e valores vazios através da linguagem Python. 
* **Exploração dos Dados** - Explorar os dados através de respostas à perguntas do CEO da empresa, achar bons insights pelas hipóteses levantadas e apresenta-los por meio de gráficos.
* **Modelagem dos Dados** - Fazer boas modelagens(correlações, reescalonamento, codificações, frequência dos dados) afim de facilitar as leituras dos modelos de Machine Learning. Achar os melhores recursos para os algoritmos.
* **Algoritmo de Machine Learning** - Com os dados modelados, vamos usar alguns algoritmos de Machine Learning de classificação para achar a melhor acurácia. Uso de Validação Cruzada e hiperparâmetros para deixa-la  ainda mais precisos os modelos e colocar em prática no final.
* **Avaliação de Algoritmo** - Comparação dos resultados dos algoritmos de classificação usados e utilizar o de melhor acurácia para colocar em prática a questão de negócios.

# 5 Análises exploratórias dos dados
**Variável de Destino**
<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/2ca4f66a-2e52-410c-8674-2d6fd0f5c47e.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/72204983-c290-401a-baa0-a9263000d991.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>


**Variável Numérica**
<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/8867efd8-74f0-4d2d-8b1b-cdc0c4f1c497.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/ea3bd12f-6d87-4558-9f31-4b757b04096d.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

**Variável Categórica**
<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/66ce2ad9-91ba-4907-bad7-6d231ecffa02.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/d2fdf1cc-8707-4f5d-8518-c8eba37795c3.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/00525bf8-5918-4619-84fb-ec4a6ed4a8ca.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/94f190f2-fd82-4a14-8bff-7b673e9b5bf1.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>


## Insights de negócio

* **H1**. A quantidade de leads do Rio de Janeiro mantém a mesma posição(2º) do somatório de leads por Estado

**Falso**: Observamos que num único anúncio, o estado do Rio de Janeiro(2º) possui, em média, mais leads que o Paraná por exemplo, mas tem menos quantidade de anúncio. Precisamos melhorar o desempenho no Paraná e aumentar a quantidade de anúncio no Rio de Janeiro.
<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/c772cd7e-109c-44ea-9f68-0cb5ccd2ce66.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H2**. A ordem de quantidade de leads por cidade é o mesmo do somatório de leads.

**Falso**: Obersamos que a cidade de Campinas é o 3º em somatório de leads, mas não está no ranking das 5 cidades em quantidade de leads. Precisamos melhorar os anúncios de algumas cidades como Curitiba, Brasília e Belo Horizonte, além de fazer mais anúncios em Campinas.

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/5bc1d3bd-344e-426c-832a-9fbd629f828b.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H3**.Pessoa Jurídica tem mais somatório de leads que Pessoa Física.

**Verdadeiro**:Observamos que é verdade. Mesmo assim, precisamos melhorar o desempenho dos anúncios de Pessoa Jurídica, pois possui muitos anúncios, mas em somatórios, a proporçaõ é menor.

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/906dd878-c971-48b3-b5d8-0fd349027eeb.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* **H4**. Anúncio com alta prioridade tem mais somatório de leads devido à urgência na venda.

**Falso**: Percebemos que é falso, pois anúncios com baixa prioridade tem mais somatório de leads. Independente disso, a proporção de prioridades é parecida quando comparada quantidade de leads e somatório de leads. Precisamos ter mais anúncios em ambas para obter mais leads.

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/29a5bc1e-cbea-41a1-b033-37a167196037.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>


# 6 Machine Learning

Usamos vários modelos de Machine Learning de classificação com o objetivo de obter a melhor acurácia e a menor quantidade de falsos positivos.**LGBMClassifier** , **CatBoostClassifier** e **XGBClassifier** foram os que possuem melhores acurácias do F1-Score que é o que procuramos e é o equilíbrio entre revocação(recall) e precisão(precision). Os três algoritmos possuem **precision**(precisão) altos e resultados bem parecidos, mas escolhemos o **LGBMClassifier** por ter uma velocidade maior no processamento. Pelo lado dos anunciantes é importante a menor quantidade possível dos **falsos positivos**(precision) também, pois o modelo estará mostrando que o anúncio obteve leads mais precisamente.Observamos que possuem alta taxa de falsos negativos(recall), mas é melhor errarmos afirmando que não tem leads. 

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/7de32533-449b-4507-9a67-8138bae54d49.jpg" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>



Se observarmos na matriz de confusão, esses 3 modelos possuem bons f1-score  que é bastante importante e uma precisão(precision) mais alta , então qualquer um poderia ser o escolhido.

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/d4329878-6cd9-4d06-a2b0-d5fc79139a1c.png" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

## 6.1 Resultados para o negócio
A principal ferramenta do Autopago, solução de tecnologia da **Webmotors**, está na segurança, pois acaba com os riscos das transações entre pessoas físicas, protegendo comprador e vendedor, uma vez que o dinheiro do comprador permanece em uma conta segura da Webmotors e só é depositado ao vendedor 24 horas após o negócio seer concretizado.

**A Webmotors cobra 1,5% do valor do veículo. Este custo pode ficar a cargo do comprador, ou do vendedor, ou mesmo os dois podem dividir o montante, com cada um custeando 0,75%.**

 



Como o modelo **LGBMClassifier** foi o escolhido entre os 3 pela rapidez no processamento e por possuir baixa porcentagem de falsos positivos(precision alta), ou seja, afirmamos com mais precisão que os dados aplicados possuem leads corretamente, erramos muito menos. Por outro lado, observamos que possui taxa maior de falsos negativos(recall baixo), mas é melhor errarmos afirmando que não tem leads quando na verdade tem (se errarmos, erramos positivamente), do que afirmarmos que possui leads sem ter, pois corremos o risco de contar algum lucro sem ter e não tomaremos nenhuma atitude para melhorar.

| Predição                | Real               | Resultado                  | 
:------------------------ | :------------------| :------------------------- | 
| Obteve lead(s)          | Não obteve lead(s) | Sem monetização e prejuízo | 
| Não obteve lead(s)      | Obteve lead(s)     | Monetização e sem prejuízo | 


## 6.2 Desempenho de Machine Learning

O modelo usado foi o **LGBMClassifier** e os resultados obtidos foram esses abaixo:

|Modelo               | Precisão             | Revocação           |f1-score              | ROC AUC            |  
:-------------------- | :--------------------| :------------------ | :--------------------| :------------------| 
|LGBMClassifier       | 0.8366 (+/- 0.3965   | 0.9972 (+/- 0.0112  | 0.8955 (+/- 0.2607   |0.8905 (+/- 0.3083 |             

# 7 Próximos passos
* Importante obter mais informações dos clientes para colocar na base de dados.
* Melhorar os desempenhos de Machine Learning
* Melhorar as análises de dados
* Usar ferramentas para uso de uma API futuramente.
  
# 8 Ferramentas utilizadas

Manipulação e limpeza dos dados: pandas, numpy

Visualização dos dados: matplotlib, seaborn

Machine learning: Classificação (scikit-learn e LGBMClassifier), seleção de features (Extra Tree Classifier) e balanceamento dos dados(SMOTETomek)

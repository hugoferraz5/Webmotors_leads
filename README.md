# Webmotors_leads
Projeto de classificação e clusterização para portfólio.O objetivo deste projeto é analisar anúncios após cinco dias de publicação para determinar se a empresa deve investir neles e recomendar os anúncios aos compradores parceiros. Para isso, desenvolveremos um modelo de aprendizado de máquina que classifica os anúncios com base em sua viabilidade para investimento e identificação de interessados.

<div align="center">
<img src="https://user-images.githubusercontent.com/91911052/180570055-64d32e4f-9123-4afa-a84b-6ab0cc5091ba.jpg" width="700px" />
</div>

# 1 O que é a Webmotors e a venda online de veículos?
* A Webmotors foi criada em 1995 e foi a primeira startup brasileira de abrangência nacional a oferecer uma forma de comprar e vender carros e motos totalmente on-line.
Sendo o primeiro catálogo e classificado on-line automobilístico brasileiro, definição inicial da Webmotors, a empresa foi idealizada por Sylvio de Barros e desenvolvida com Marcelo Zamprogna Krug e a Team Systems, empresa de soluções para internet no Brasil.
* Os dados mostram que 2021, a venda online em todas as plataformas de vendas somadas tiveram um aumento de apenas 3% na venda de carros em relação ao ano anterior, 2020, totalizando 2,120 milhões de unidades no país.
* Com a consolidação dos meios digitais como aliados em nossas vidas, nada mais habitual do que utilizar novas ferramentas e recursos para comprar e vender carros pela internet, afinal, a instantaneidade e a comodidade são praticamente requisitos para quem deseja facilidade para negociar.

# 2 Apresentação
Neste projeto, propusemos um modelo de classificação com o objetivo de prever a viabilidade de anúncios para investimento e indicação a compradores parceiros após cinco dias de publicação. Inicialmente, clusterizamos o conjunto de dados para identificar suas características e estabelecer um padrão. Os resultados obtidos mostraram que cada cluster é dividido com base no interesse dos compradores (leads, visualizações dos anúncios e cliques nos telefones). Consequentemente, nomeamos cada cluster como Ideal, Quase_Ideal, Normal e Desqualificado, sendo Ideal a classificação indicada. Devido à dificuldade de identificar um padrão apenas com dados anteriores à publicação, inserimos dados futuros e adicionamos um contexto com o objetivo de maximizar a monetização da empresa.

O processo de clustering foi fundamental para entender melhor o comportamento dos anúncios e definir os padrões de interesse dos compradores. Utilizamos técnicas de aprendizado de máquina para agrupar os dados, o que nos permitiu categorizar os anúncios de maneira mais precisa. Após o anúncio ser publicado, monitoramos suas métricas por cinco dias. Com base nesses dados, aplicamos nosso modelo de classificação para determinar a viabilidade do anúncio.

Além disso, a implementação desse modelo visa não apenas melhorar a precisão das indicações aos compradores parceiros, mas também otimizar os investimentos dos anunciantes, maximizando os retornos e minimizando os riscos. Este sistema proporciona uma abordagem mais estruturada e baseada em dados para a tomada de decisões estratégicas no mercado de anúncios. 

Os compradores parceiros pagam uma mensalidade em troca de indicações de possíveis interessados nos anúncios classificados como Ideal. A escolha do período de 5 dias foi estratégica para observar a evolução do anúncio em um curto prazo, permitindo uma resposta rápida e eficaz. Os compradores parceiros são alertados imediatamente quando um anúncio é classificado como Ideal, garantindo que possam agir rapidamente em oportunidades de alta qualidade. Por fim, obtivemos ótimos resultados. Algumas informações foram coletadas neste link:
<a href="https://www.webmotors.com.br/wm1/dinheiro-e-economia/webmotors-revoluciona-compra-venda#:~:text=A%20Webmotors%20cobra%201%2C5,um%20custeando%200%2C75%25.">siteWebmotors</a>

Para facilitar o trabalho dos tomadores de decisão e gerência, implantamos o modelo no <a href="https://docs.google.com/spreadsheets/d/11Ww1iAl8CqcZaQaFKDQnVmj4dTKqTmSD40Q5Mck-OeA/edit?gid=0#gid=0">Google Sheets</a> , no qual foi utilizado o JavaScript para solicitações API ao modelo implantado e o resultado inserido na planilha.

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
* O interesse dos compradores (leads, visualizações de anúncios e cliques nos telefones) será um indicador confiável e consistente da viabilidade dos anúncios.
* O comportamento dos usuários durante os primeiros cinco dias após a publicação do anúncio é representativo de seu desempenho futuro.
* Os gráficos ajudaram a ter mais clareza nas análises.
* O processo de clustering usado para dividir os anúncios em categorias como Ideal, Quase_Ideal, Normal e Desqualificado é eficaz e reflete a realidade do mercado.
* A integração do modelo de classificação ao Google Sheets usando JavaScript e APIs funcionará de maneira eficiente e sem problemas técnicos significativos.
* A equipe de vendas será capaz de reagir rapidamente às classificações fornecidas pelo modelo, aproveitando as oportunidades identificadas.

# 4 Passo a passo da solução

* **Questão de Negócios** - Prever a viabilidade de futuros anúncios da Webmotors após 5 dias de sua implementação e identificar rapidamente se vale a pena investir nesses anúncios e indicar seus leads a compradores parceiros, visando aumentar o lucro da empresa.

* **Entendimento do Negócio** - Analisar o histórico dos anúncios da Webmotors por meio dos dados disponíveis. Utilizar técnicas de clusterização para identificar padrões de interesse dos compradores. Com base nessas informações, aplicar técnicas de aprendizado de máquina de classificação para prever a viabilidade de futuros anúncios implementados 5 dias após sua publicação.
* **Coleta de Dados** - Coletar os dados fictícios da empresa Webmotors, incluindo informações sobre leads, visualizações de anúncios e interações dos usuários.
* **Limpeza dos Dados** - Realizar a limpeza dos dados, tratando valores discrepantes e vazios, utilizando a linguagem Python e técnicas adequadas de pré-processamento de dados para garantir a qualidade dos dados utilizados no modelo. 
* **Exploração dos Dados** - Explorar os dados através de respostas à perguntas do CEO da empresa, achar bons insights pelas hipóteses levantadas e apresenta-los por meio de gráficos.Além disso, explorar os dados por meio de análises descritivas e visualizações, utilizando insights obtidos com a clusterização para responder às perguntas do CEO da empresa e identificar padrões relevantes que possam influenciar a geração de leads nos anúncios da Webmotors. O projeto pode ser encontrado no <a href="https://github.com/hugoferraz5/Webmotors_leads/blob/main/Classifica%C3%A7%C3%A3o_webmotors.ipynb">Webmotors</a>
* **Modelagem dos Dados** - Fazer boas modelagens(correlações, reescalonamento, codificações, frequência dos dados) afim de facilitar as leituras dos modelos de Machine Learning. Achar os melhores recursos para os algoritmos.
* **Algoritmo de Machine Learning** - Com os dados modelados, vamos usar alguns algoritmos de Machine Learning de clusterização para classifica-los de acordo com suas padronizações e algoritmos de Machine Learning de classificação para achar a melhor acurácia. Uso de Validação Cruzada e hiperparâmetros para deixa-la  ainda mais precisos os modelos e colocar em prática no final.
* **Avaliação de Algoritmo** - Comparação dos resultados dos algoritmos de clusterização(Silhouette Score) e classificação(Precisão, Recall, Acurácia, F1-Score, Brier Score Loss, Densidade de Probabilidade) usados e utilizar os de melhor acurácia para apresentar o modelo completo traduzido ao tomador de decisão e gerentes para que eles decidam sobre sua implementação.
* **Implantação** - O modelo foi implantado na nuvem AWS para garantir escalabilidade e disponibilidade. Além disso, foi utilizado o ngrok para implementação, proporcionando uma solução flexível e acessível pela planilha do <a href="https://docs.google.com/spreadsheets/d/11Ww1iAl8CqcZaQaFKDQnVmj4dTKqTmSD40Q5Mck-OeA/edit?gid=0#gid=0">Google Sheets</a> . Essa abordagem permite acesso rápido e fácil ao modelo de qualquer lugar, facilitando a integração com as ferramentas de trabalho da equipe de vendas.

![Imagem 1](https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/c8b25f44-ce0c-4a22-beff-2ed98c22788d)
  
  

![Imagem 2](https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/68bc429d-1dc3-4831-9bed-9527603af24a)



# 5 Principais insights
* Anúncios com baixa prioridade possuem mais somatórios de leads

* Os estados de Rio de Janeiro, Minas Gerais e Paraná são os que possuem mais somatórios de leads após São Paulo
* O estado de São Paulo é o líder com mais anúncios

* A cidade de São Paulo tem maior quantidade de anúncios disparado

* Pessoas Físicas produzem anúncios com mais qualidade que Pessoas Jurídicas

# 6 Machine Learning
## 6.1 Clusterização
Como o conjunto de dados possui a variável alvo numérica leads, mas o objetivo da questão de negócios é transformá-la em um problema de classificação, tentei inicialmente dividir essa variável em subcategorias em cima desses leads. No entanto, essa abordagem não gerou bons resultados, possivelmente porque as subcategorias não refletiam adequadamente o padrão dos dados. Então, optei por utilizar métodos de clusterização para encontrar uma divisão coerente dos dados, que pudesse ser utilizada em modelos de classificação com bons resultados.O modelo escolhido foi o `K-Means com espaço UMAP embedded e 4 clusters`. 

Para uma análise mais aprofundada entre modelos e espaços de características, comparamos apenas o Silhouette Score. Uma explicação simples da métrica e seu significado é que mede a distância entre os clusters e o quão compacto é um cluster. A métrica pode ser interpretada analisando os valores das distâncias. Para uma pontuação positiva, com valor máximo de 1, significa que os clusters são compactos e distantes entre si, porém o mais próximo de -1 significa que os clusters são grandes e/ou sobrepostos.Ele possui bom valor da métrica **(~0.47 para SS)**, de forma a garantir mais características individuais de cada cluster.

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/39e57463-e92a-45b8-9094-a1711fff2c4b" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

Após escolha, consegui construir um modelo de clustering que coleta dados de anúncios, agrupa-os em 4 grupos diferentes e extrai suas principais características para atribuir à uma eterminada classe. As classes determinadas são **Ideais, Quase_Ideais, Normal e Desqualificado**.

![Imagem 1](https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/50a532d0-216a-4c10-be9c-407aa984c690)

### 6.1.1 Perfil dos clusters
* Cluster 0: Apresenta as maiores médias de leads e cliques_telefone sendo considerado o cluster Ideais

* Cluster 2: Possui a segunda maior média de leads e cliques_telefone, além da segunda maior média de views. Portanto, é classificado como Quase_Ideais

* cluster 1: Embora tenha uma baixa média de leads possui a maior média de views, indicando que os clientes demonstram algum interesse nesses anúncios. Assim, é considerado Normal

* Cluster 3: Possui baixas médias de leads, views e cliques_telefone, embora os valores de views sejam um pouco maiores do que os do Cluster 0, classificando-o como Desqualificado

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/445fbbf5-8119-4296-a518-b28f21e75876" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

  
## 6.2 Classificação
Neste problema de negócio, inicialmente tentamos identificar padrões utilizando dados anteriores à publicação dos anúncios. No entanto, os resultados dos modelos não foram satisfatórios. Portanto, decidimos incorporar dados futuros e adicionar um contexto adicional, com o objetivo de maximizar a monetização da empresa. Além disso, como a clusterização resultou em uma boa segmentação dos dados, é provável que as métricas de classificação apresentem resultados bastante elevados.

### 6.2.1 Comparação dos modelos
Para o problema de classificação usamos  o algoritmo `Random Forest Classifier` que **não é o melhor para precision e recall referentes às classes 1 e 3**, mas possui o **melhor resultado combinado para as classes 0 e 2** que são as que importam. O precision se torna bem importante, pois quanto mais acertarmos os anúncios que realmente pertencem à 0 e 2, melhor para o negócio. Possui uma **menor porcentagem de falsos negativos(recall) que o CatBoostClassifier da classe 2**, mas é **superior no precision e nas métricas das outras classes**, além de que é bem equilibrado com o Balanced Forest Classifier, sendo superior em tudo.

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/6c6ff208-8004-40dc-9096-90fe8c076f7a" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/d0c06209-b6bd-4a8f-8d17-272599675ec6" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/8b7d33b1-5bce-487a-91a1-ed3277be6232" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

Embora `Balanced Random Forest Classifier`, `Random Forest Classifier` e `LGBMClassifier` aparentem ter os melhores resultados, usamos o `Random Forest Classifier` por ser levemente melhor, além de possuir os melhores resultados para as classes 0 e 2(Ideal e Quase_Ideal) que são os que importam.

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/5952851b-64d2-4225-a6e8-77bb1320e824" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

<img src="https://github.com/hugoferraz5/Webmotors_leads/assets/91911052/7d6cca90-6788-4d39-928c-61966654b9de" alt="pic1" style="zoom:60% ;" />
<spacer type="horizontal" width="10" height="10">  </spacer>

* Feito o gráfico da curva ROC, observamos como os modelos `Random Forest Classifier` e `Balanced Random Forest Classifier` são bons comparados à reta sem habilidade(aproximadamente 99%).
* Ao analisar o gráfico de probabilidades de densidades, observamos que as distribuições estão concentradas em torno de 0 ou 1. Isso indica que o modelo classifica as observações com altas probabilidades para uma determinada classe. Aplicamos os modelos `Random Forest Classifier` e `Balanced Random Forest Classifier`, e os resultados foram bastante semelhantes, demonstrando que ambos os modelos tiveram um bom desempenho.
  
### 6.2.2 Modelo escolhido
O algoritmo escolhido foi o **Random Forest Classifier**.

||Average precision |Average recall  |Average f1-score            | Average roc_auc  |
:----------|:------------------------| :-----------      | :------------------ | :-----------------------------|
| Random Forest Classifier|0.9789 (+/- 0.0044) |0.9778 (+/- 0.0054)| 0.9783 (+/- 0.0045)|0.9991 (+/- 0.0004)     |
| Random Forest Classifier (Ajustado)|0.9799 (+/- 0.0058)| 0.9797 (+/- 0.0068)| 0.9797 (+/- 0.0060) |0.9982 (+/- 0.0011)|

Com o modelo ajustado, percebemos que as métricas, principalmente **f1-score** e **recall** tiveram um melhor desempenho comparado ao modelo simples. Além disso, observamos também na **matriz de confusão** um melhor desempenho das mesmas métricas nas classes **0 e 2(Ideal e Quase_Ideal)** que são as que importam, pois queremos anúncios que gerem mais leads.

# 7 Performance de Negócio
A principal ferramenta do Autopago, solução de tecnologia da Webmotors, está na segurança, pois acaba com os riscos das transações entre pessoas físicas, protegendo comprador e vendedor, uma vez que o dinheiro do comprador permanece em uma conta segura da Webmotors e só é depositado ao vendedor 24 horas após o negócio seer concretizado.

**A Webmotors cobra 1,5% do valor do veículo. Este custo pode ficar a cargo do comprador, ou do vendedor, ou mesmo os dois podem dividir o montante, com cada um custeando 0,75%.**

Usaremos o **monitoramento contínuo** para o problema de negócio, que envolve dados de diversos anúncios na Webmotors, com a variável alvo criada por meio de clusterização, resultando em 4 classes: **Ideal (0)**, **Quase_Ideal (2)**, **Normal (1)** e **Desqualificada (3)**. O modelo `Random Forest Classifier` apresentou o melhor desempenho para esta tarefa. O objetivo é identificar quais anúncios futuros, após 5 dias, têm maior probabilidade de pertencer às classes 0 ou 2, consideradas as mais atraentes para os compradores, pois indicam maior interesse potencial. Após um anúncio ser classificado em uma dessas duas classes, o gerente poderá tomar ações específicas e investimento para destacá-lo e recomendar os interessados por esse anúncio para compradores parceiros, visando aumentar suas chances de venda.

O algoritmo `Random Forest Classifier` não é o melhor para **precision** e **recall** referentes às classes 1 e 3, mas possui o melhor resultado combinado para as classes 0 e 2 que são as que importam. O **precision** se torna bem importante, pois quanto mais acertarmos os anúncios que realmente pertencem à 0 e 2, melhor para o negócio. Possui uma menor porcentagem de **falsos negativos(recall)** que o `CatBoostClassifier` da classe 2, mas é superior no **precision** e nas métricas das outras classes, além de que é bem equilibrado com o `Balanced Forest Classifier`, sendo superior em tudo.

Cluster | Predição      | Real        | Resultado                  | Cenário
| :-------|:-------------- | :-----------| :------------------------- | ----------- |
| 0| Ideal         | Ideal       | Monetização e sem prejuízo     | Melhor cenário
| 2| Quase_ideal   | Quase_ideal | Monetização e sem prejuízo     | Bom cenário
| 3| Desqualificado    | Ideal   | Monetização e sem prejuízo | Bom cenário
| 0| Ideal      | Desqualificado     | Sem monetização e prejuízo | Pior cenário
| 1| Normal          | Normal | Sem monetização e sem prejuízo | Médio cenário
| 3| Desqualificado      | Desqualificado     | Sem monetização e prejuízo | Pior cenário
            

# 7 Próximos passos
* Importante obter mais informações dos clientes para colocar na base de dados.
* Melhorar as análises de dados
* Usar outras ferramentas para uso de API.
  
# 8 Ferramentas utilizadas

Manipulação e limpeza dos dados: pandas, numpy

Visualização dos dados: matplotlib, seaborn

Machine learning: Clusterização(PCA, UMAP e Incorporação baseada em árvore) e Classificação (scikit-learn e LGBMClassifier), seleção de features (Extra Tree Classifier) e balanceamento dos dados(SMOTETomek)

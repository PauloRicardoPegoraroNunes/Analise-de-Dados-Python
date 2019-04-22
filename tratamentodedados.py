import pandas as pd
#pode ser usado qualquer arquivo csv
#link para o dowload do arquivo usado aqui http://dados.gov.br/dataset/mec-pronatec-eptc/resource/0abee23b-9e79-4893-b284-6882f9d39fdd
#caso use outro arquivo terá que mudar na variavel df abaixo 

df = pd.read_csv('MAT_ATENDIDAS_RF_EPCT_2011_CSV.csv',
                 sep=';', encoding='cp1252')

# le as primeiras 5 linhas do csv
x = df.head()
# mostra os tipos de dados
y = df.dtypes
# seleciona os dados a ser mostrado
c = df['CODIGO_IDENTIFICACAO_MEC'].value_counts()


print(x)
print(y)
print(c)




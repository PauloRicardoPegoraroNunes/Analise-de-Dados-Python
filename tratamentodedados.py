import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('MAT_ATENDIDAS_RF_EPCT_2011_CSV.csv',
                 sep=';', encoding='cp1252')

# le as primeiras 5 linhas do csv
x = df.head()

# mostra os tipos de dados
y = df.dtypes

# seleciona os dados a ser mostrado
c = df['CODIGO_IDENTIFICACAO_MEC'].value_counts()
print(y)
print(c)
plt.show()



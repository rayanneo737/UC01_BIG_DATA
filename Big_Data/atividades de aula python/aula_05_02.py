import pandas as pd
# inpotando dados da base de dados
endereco_dados = 'BASES\Financeira.csv'
#criando o DataFrame
df_financeira = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')
#Exibindo DataFrame
print("----- Dados financeiros ----")
print(df_financeira.head())
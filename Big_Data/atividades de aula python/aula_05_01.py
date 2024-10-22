#pip install xlrd - biblioteca para manipular arquivos xlsx (Terminal)
#pip install openpysl - biblioteca para manipular arquivos do excel
import pandas as pd
# inpotando dados da base de dados
endereco_dados = 'BASES\ENEM_2020_2023.xlsx'
#criando o DataFrame
df_enem = pd.read_excel(endereco_dados)
print("-----Quantidade de inscritos no enem ----")
print(df_enem.head())
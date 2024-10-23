import pandas as pd

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
print('\n---- OBTENDO DADOS GERAIS SOBRE OCORRÊNCIAS ----')
print(df_ocorrencias.head())

df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(["roubo_veiculo"]).reset_index()
print('\n---- OBTENDO DADOS SOBRE VEICULOS ----')
print(df_roubo_veiculo.head())

#Ano e Homincídio doloso
import pandas as pd

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

#criando dataframe ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
print('\n---- OBTENDO DADOS GERAIS SOBRE OCORRÊNCIAS ----')
print(df_ocorrencias.head())

df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
print('\n---- OBTENDO DADOS SOBRE VEICULOS ----')
print(df_roubo_veiculo.head())

#Df homicio doloso por ano
df_ano_hom_doloso = df_ocorrencias[['ano','hom_doloso']]
df_ano_hom_doloso = df_ano_hom_doloso.groupby(['ano']).sum(['hom_doloso']).reset_index()
print('\n---- OBTENDO DADOS SOBRE VEICULOS ----')
print(df_ano_hom_doloso.head())

#Df homicio doloso e culposo por delegacias
df_delegacias = df_ocorrencias[['cisp','hom_doloso','hom_culposo']]
df_delegacias = df_delegacias.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index()
print('\n---- OBTENDO DADOS SOBRE VEICULOS ----')
print(df_delegacias.head())
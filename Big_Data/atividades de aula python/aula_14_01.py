import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_lesao_corp_dolosa = df_ocorrencias[['cisp','ano','lesao_corp_dolosa']]
df_lesao_corp_dolosa = df_lesao_corp_dolosa[df_lesao_corp_dolosa['ano'].isin([2022,2023,2024])]
df_lesao_corp_dolosa = df_lesao_corp_dolosa.groupby(['cisp']).sum(['lesao_corp_dolosa']).reset_index()

df_lesao_corp_culposa_dolosa = df_ocorrencias[['cisp','ano','lesao_corp_dolosa','lesao_corp_culposa']]
df_lesao_corp_culposa_dolosa = df_lesao_corp_culposa_dolosa[df_lesao_corp_culposa_dolosa['ano'].isin([2022,2023,2024])]
df_lesao_corp_culposa_dolosa = df_lesao_corp_culposa_dolosa.groupby(['cisp']).sum(['lesao_corp_dolosa','lesao_corp_culposa']).reset_index()

print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_lesao_corp_dolosa.head())

# Criando o array dos roubos de veiculos
array_lesao_corp_dolosa = np.array(df_lesao_corp_dolosa["lesao_corp_dolosa"])

# Obtendo a média dos roubos de veiculos
media_lesao_corp_dolosa = np.mean(array_lesao_corp_dolosa)

# Obtendo a mediana dos roubos de veiculos
mediana_lesao_corp_dolosa = np.median(array_lesao_corp_dolosa)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_lesao_corp_dolosa = abs((media_lesao_corp_dolosa - mediana_lesao_corp_dolosa) / mediana_lesao_corp_dolosa) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_lesao_corp_dolosa = np.max(array_lesao_corp_dolosa)
minimo_lesao_corp_dolosa = np.min(array_lesao_corp_dolosa)

# Obtendo a amplitude dos roubos de veiculos
amplitude_lesao_corp_dolosa = maximo_lesao_corp_dolosa - minimo_lesao_corp_dolosa

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.25, method='weibull')
q2_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.50, method='weibull')
q3_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.75, method='weibull')
iqr_lesao_corp_dolosa = q3_lesao_corp_dolosa - q1_lesao_corp_dolosa

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_lesao_corp_dolosa = q3_lesao_corp_dolosa + (1.5 * iqr_lesao_corp_dolosa)
limite_inferior_lesao_corp_dolosa = q1_lesao_corp_dolosa - (1.5 * iqr_lesao_corp_dolosa)

# Filtrando o DataFrame roubos de veículos
df_lesao_corp_dolosa_outliers_superiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] > limite_superior_lesao_corp_dolosa]
df_lesao_corp_dolosa_outliers_inferiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] < limite_inferior_lesao_corp_dolosa]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_lesao_corp_dolosa = np.var(array_lesao_corp_dolosa)
distancia_var_lesao_corp_dolosa = variancia_lesao_corp_dolosa / (media_lesao_corp_dolosa**2)
desvio_padrao_lesao_corp_dolosa = np.std(array_lesao_corp_dolosa)
coeficiente_var_lesao_corp_dolosa = desvio_padrao_lesao_corp_dolosa / media_lesao_corp_dolosa

correlacao_lesao_corp = np.corrcoef(df_lesao_corp_culposa_dolosa['lesao_corp_dolosa'],df_lesao_corp_culposa_dolosa['lesao_corp_culposa'])[0,1]

# Exibindo os dados sobre os roubos de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE AS LESÕES COMPORTAIS DOLOROSAS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média das lesões corporais culposas é de {media_lesao_corp_dolosa:.0f}")
print(f"A mediana das lesões corporais culposas é de {mediana_lesao_corp_dolosa:.0f}")
print(f"A distância entre a média e a mediana das lesões corporais culposas é de {distancia_lesao_corp_dolosa:.2f} %")
print(f"O menor valor das lesões corporais culposas é de {minimo_lesao_corp_dolosa:.0f}")
print(f"O maior valor das lesões corporais culposas é de {maximo_lesao_corp_dolosa:.0f}")
print(f"A amplitude dos valores das lesões corporais culposas é de {amplitude_lesao_corp_dolosa:.0f}")
print(f"O valor do q1 - 25% das lesões corporais culposas é de {q1_lesao_corp_dolosa:.0f}")
print(f"O valor do q2 - 50% das lesões corporais culposas é de {q2_lesao_corp_dolosa:.0f}")
print(f"O valor do q3 - 75% das lesões corporais culposas é de {q3_lesao_corp_dolosa:.0f}")
print(f"O valor do iqr = q3 - q1 das lesões corporais culposas é de {iqr_lesao_corp_dolosa:.0f}")
print(f"O limite inferior das lesões corporais culposas é de {limite_inferior_lesao_corp_dolosa:.0f}")
print(f"O limite superior das lesões corporais culposas é de {limite_superior_lesao_corp_dolosa:.0f}")
print(f"A variância das lesões corporais culposas é de {variancia_lesao_corp_dolosa:.0f}")
print(f"A distância da variância X média das lesões corporais culposas é de {distancia_var_lesao_corp_dolosa:.0f}")
print(f"O desvio padrão das lesões corporais culposas é de {desvio_padrao_lesao_corp_dolosa:.0f}")
print(f"O coeficiente de variação das lesões corporais culposas é de {coeficiente_var_lesao_corp_dolosa:.0f}")
print(f"A correlação das lesões corporais culposas é de {correlacao_lesao_corp:.1f}")

if len(df_lesao_corp_dolosa_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_lesao_corp_dolosa_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_lesao_corp_dolosa_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_lesao_corp_dolosa_outliers_superiores)

# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre as lesões corporais culposas')

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot das lesões corporais culposas')
plt.boxplot(array_lesao_corp_dolosa,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,2)
plt.title('Comparativo das lesões corporais culposas')
plt.scatter(df_lesao_corp_culposa_dolosa['lesao_corp_dolosa'],df_lesao_corp_culposa_dolosa['lesao_corp_culposa'],edgecolors='black',color='green')
plt.xlabel('Lesão Corporal Dolosa')
plt.ylabel('Lesão Corporal Culposa')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_lesao_corp_dolosa_outliers_superiores_order = df_lesao_corp_dolosa_outliers_superiores.sort_values(by='lesao_corp_dolosa',ascending=True)
plt.title('Ranking das Delegacias')
plt.barh(df_lesao_corp_dolosa_outliers_superiores_order['cisp'].astype(str),df_lesao_corp_dolosa_outliers_superiores_order['lesao_corp_dolosa'])

plt.subplot(2,2,4)
plt.title('Medidas Descritivas das lesões comporais culposas')
plt.axis('off')
plt.text(0.1,0.9,f'Média das lesões corporais culposas é de: {media_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana das lesões corporais culposas é de: {mediana_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana das lesões corporais culposas é de: {distancia_lesao_corp_dolosa:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor das lesões corporais culposas é de: {maximo_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor das lesões corporais culposas é de: {minimo_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média das lesões corporais culposas é de: {distancia_var_lesao_corp_dolosa:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação das lesões corporais culposas é de: {coeficiente_var_lesao_corp_dolosa:.2f}',fontsize=12)
plt.text(0.1,0.2,f'Correlação entre as lesões corporais culposas é de: {correlacao_lesao_corp:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()
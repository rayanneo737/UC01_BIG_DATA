import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_recuperacao_veiculos = df_ocorrencias[['aisp','ano','recuperacao_veiculos']]
df_recuperacao_veiculos = df_recuperacao_veiculos[df_recuperacao_veiculos['ano'].isin([2022,2023])]
df_recuperacao_veiculos = df_recuperacao_veiculos.groupby(['aisp']).sum(['recuperacao_veiculos']).reset_index()



print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_recuperacao_veiculos.head())

array_recuperacao_veiculos = np.array(df_recuperacao_veiculos["recuperacao_veiculos"])

# Obtendo a média dos roubos de veiculos
media_recuperacao_veiculos = np.mean(array_recuperacao_veiculos)

# Obtendo a mediana dos roubos de veiculos
mediana_recuperacao_veiculos = np.median(array_recuperacao_veiculos)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_recuperacao_veiculos = abs((media_recuperacao_veiculos - mediana_recuperacao_veiculos) / mediana_recuperacao_veiculos) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_recuperacao_veiculos = np.max(array_recuperacao_veiculos)
minimo_recuperacao_veiculos = np.min(array_recuperacao_veiculos)

# Obtendo a amplitude dos roubos de veiculos
amplitude_recuperacao_veiculos = maximo_recuperacao_veiculos - minimo_recuperacao_veiculos

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.25, method='weibull')
q2_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.50, method='weibull')
q3_recuperacao_veiculos = np.quantile(array_recuperacao_veiculos, 0.75, method='weibull')
iqr_recuperacao_veiculos = q3_recuperacao_veiculos - q1_recuperacao_veiculos

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_recuperacao_veiculos = q3_recuperacao_veiculos + (1.5 * iqr_recuperacao_veiculos)
limite_inferior_recuperacao_veiculos = q1_recuperacao_veiculos - (1.5 * iqr_recuperacao_veiculos)

# Filtrando o DataFrame roubos de veículos
df_recuperacao_veiculos_outliers_superiores = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] > limite_superior_recuperacao_veiculos]
df_recuperacao_veiculos_outliers_inferiores = df_recuperacao_veiculos[df_recuperacao_veiculos['recuperacao_veiculos'] < limite_inferior_recuperacao_veiculos]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_recuperacao_veiculos = np.var(array_recuperacao_veiculos)
distancia_var_recuperacao_veiculos = variancia_recuperacao_veiculos / (media_recuperacao_veiculos**2)
desvio_padrao_recuperacao_veiculos = np.std(array_recuperacao_veiculos)
coeficiente_var_recuperacao_veiculos = desvio_padrao_recuperacao_veiculos / media_recuperacao_veiculos

print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS ROUBOS DE VEÍCULOS -----------")
print('------------------ Medidas de Tendência Central ---------------------\n')
print(f"A média das recuperações dos veículos é {media_recuperacao_veiculos:.0f}")
print(f"A mediana das recuperações dos veículos é {mediana_recuperacao_veiculos:.0f}")
print(f"A distância entre a média e a mediana das recuperações dos veículos é {distancia_recuperacao_veiculos:.2f} %")
print(f"O menor valor das recuperações dos veículos é {minimo_recuperacao_veiculos:.0f}")
print(f"O maior valor das recuperações dos veículos é {maximo_recuperacao_veiculos:.0f}")
print(f"A amplitude dos valores das recuperações dos veículos é {amplitude_recuperacao_veiculos:.0f}")
print(f"O valor do q1 - 25% das recuperações dos veículos é {q1_recuperacao_veiculos:.0f}")
print(f"O valor do q2 - 50% das recuperações dos veículos é {q2_recuperacao_veiculos:.0f}")
print(f"O valor do q3 - 75% das recuperações dos veículos é {q3_recuperacao_veiculos:.0f}")
print(f"O valor do iqr = q3 - q1 das recuperações dos veículos é {iqr_recuperacao_veiculos:.0f}")
print(f"O limite inferior das recuperações dos veículos é {limite_inferior_recuperacao_veiculos:.0f}")
print(f"O limite superior das recuperações dos veículos é {limite_superior_recuperacao_veiculos:.0f}")
print(f"A variância das recuperações dos veículos é {variancia_recuperacao_veiculos:.0f}")
print(f"A distância da variância X média das recuperações dos veículos é {distancia_var_recuperacao_veiculos:.0f}")
print(f"O desvio padrão das recuperações dos veículos é {desvio_padrao_recuperacao_veiculos:.0f}")
print(f"O coeficiente de variação das recuperações dos veículos é {coeficiente_var_recuperacao_veiculos:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_recuperacao_veiculos_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_recuperacao_veiculos_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_recuperacao_veiculos_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_recuperacao_veiculos_outliers_superiores)

# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise sobre as recuperações de veículos')

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot das recuperações dos veículos')
plt.boxplot(array_recuperacao_veiculos,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,2)
plt.title('Histograma das recuperações dos veículos')
plt.hist(array_recuperacao_veiculos,bins=100,edgecolor='black')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_recuperacao_veiculos_outliers_superiores_order = df_recuperacao_veiculos_outliers_superiores.sort_values(by='recuperacao_veiculos',ascending=True)
plt.title('Ranking das Delegacias com Outliers Superiores')
plt.barh(df_recuperacao_veiculos_outliers_superiores_order['aisp'].astype(str),df_recuperacao_veiculos_outliers_superiores_order['recuperacao_veiculos'])

# posição 04: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos Roubos de Veículos')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos Roubos de Veículos {media_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos Roubos de Veículos {mediana_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos Roubos de Veículos {distancia_recuperacao_veiculos:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos Roubos de Veículos {maximo_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos Roubos de Veículos {minimo_recuperacao_veiculos:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos Roubos de Veículos {distancia_var_recuperacao_veiculos:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos Roubos de Veículos {coeficiente_var_recuperacao_veiculos:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('---- OBTENDO DADOS ----')
# Importando a base de dados financeira.csv
endereco_dados = 'BASES\Financeira.csv'

# Criando o DataFrame financeira
df_financeira = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

# Exibindo a base de dados financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_financeira.head())

# Criando o array da renda e do valor emprestado
# Os arrays são estruturas de dados que armazenam uma coleção de dados e computacionalmente mais eficiente para cálculos estatísticos. Faz parte da biblioteca numpy.
array_financeira_renda = np.array(df_financeira["Renda"])
array_financeira_Vlr_emprestado = np.array(df_financeira["Vlr_emprestado"])

# Obtendo a média da renda e do valor emprestado
# Se a média for maior que 25% em relação a mediana, a distribuição será assimétrica, podendo existir outliers. Caso contrário a distribuição será simétrica.
media_renda = np.mean(array_financeira_renda)
media_Vlr_emprestado = np.mean(array_financeira_Vlr_emprestado)

# Obtendo a mediana da renda e do valor emprestado
mediana_renda = np.median(array_financeira_renda)
mediana_Vlr_emprestado = np.median(array_financeira_Vlr_emprestado)

# Obtendo a distância da renda e do valor emprestado
distancia_renda = abs((media_renda - mediana_renda) / mediana_renda) * 100
distancia_Vlr_emprestado = abs((media_Vlr_emprestado - mediana_Vlr_emprestado) / mediana_Vlr_emprestado) * 100

# Obtendo o maior e o menor valor da renda e do valor emprestado
maior_renda = np.max(array_financeira_renda)
maior_Vlr_emprestado = np.max(array_financeira_Vlr_emprestado)
menor_renda = np.min(array_financeira_renda)
menor_Vlr_emprestado = np.min(array_financeira_Vlr_emprestado)

# Obtendo a amplitude da renda e do valor emprestado
amplitude_renda = maior_renda - menor_renda
amplitude_Vlr_emprestado = maior_Vlr_emprestado - menor_Vlr_emprestado

# Obtendo os Quartis da renda e do valor emprestado - Método weibull
q1_renda = np.quantile(array_financeira_renda, 0.25, method='weibull')
q2_renda = np.quantile(array_financeira_renda, 0.50, method='weibull')
q3_renda = np.quantile(array_financeira_renda, 0.75, method='weibull')
iqr_renda = q3_renda - q1_renda

q1_Vlr_emprestado = np.quantile(array_financeira_Vlr_emprestado, 0.25, method='weibull')
q2_Vlr_emprestado = np.quantile(array_financeira_Vlr_emprestado, 0.50, method='weibull')
q3_Vlr_emprestado = np.quantile(array_financeira_Vlr_emprestado, 0.75, method='weibull')
iqr_Vlr_emprestado = q3_Vlr_emprestado - q1_Vlr_emprestado

# Identificando os outliers superiores e inferiores da renda e do valor emprestado
limite_superior_renda = q3_renda + (1.5 * iqr_renda)
limite_inferior_renda = q1_renda - (1.5 * iqr_renda)

limite_superior_Vlr_emprestado = q3_Vlr_emprestado + (1.5 * iqr_Vlr_emprestado)
limite_inferior_Vlr_emprestado = q1_Vlr_emprestado - (1.5 * iqr_Vlr_emprestado)

# Filtrando o DataFrame financeira
df_financeira_renda_outliers_superiores = df_financeira[df_financeira['Renda'] > limite_superior_renda]
df_financeira_renda_outliers_inferiores = df_financeira[df_financeira['Renda'] < limite_inferior_renda]

df_financeira_Vlr_emprestado_outliers_superiores = df_financeira[df_financeira['Vlr_emprestado'] > limite_superior_Vlr_emprestado]
df_financeira_Vlr_emprestado_outliers_inferiores = df_financeira[df_financeira['Vlr_emprestado'] < limite_inferior_Vlr_emprestado]

#Obtendo as medidas de dispersão da renda e do valor emprestado
variancia_renda = np.var(array_financeira_renda)
distancia_renda = variancia_renda /(media_renda**2)
desvio_padrao_renda = np.std(array_financeira_renda)
coeficiente_var_renda = desvio_padrao_renda/media_renda

variancia_emprestado = np.var(array_financeira_Vlr_emprestado)
distancia_emprestado = variancia_emprestado /(media_Vlr_emprestado**2)
desvio_emprestado = np.std(array_financeira_Vlr_emprestado)
coeficiente_emprestado = desvio_emprestado/media_Vlr_emprestado

# Exibindo os dados sobre a renda
print('\nOBTENDO INFORMAÇÕES SOBRE RENDA')
print('Medidas de Tendência Central')
print(f"\nA média das rendas dos clientes é R$ {media_renda:.2f}")
print(f"A mediana das rendas dos clientes é R$ {mediana_renda:.2f}")
print(f"A distância entre a média e a mediana das rendas dos clientes é  {distancia_renda:.2f} %")
print(f"O maior valor das rendas dos clientes é R$ {maior_renda:.2f}")
print(f"O menor valor das rendas dos clientes é R$ {menor_renda:.2f}")
print(f"A amplitude das rendas dos clientes é R$ {amplitude_renda:.2f}")
print(f"O valor do q1 - 25% da renda é R$ {q1_renda:.2f}")
print(f"O valor do q2 - 50% da renda é R$ {q2_renda:.2f}")
print(f"O valor do q3 - 75% da renda é R$ {q3_renda:.2f}")
print(f"O valor do iqr = q3 - q1 da renda é R$ {iqr_renda:.2f}")
print(f"O limite inferior da renda é R$ {limite_inferior_renda:.2f}")
print(f"O limite superior da renda é R$ {limite_superior_renda:.2f}")
print(f"A variancia das rendas dos clientes é {variancia_renda:.2f}")
print(f"A distancia da variância X média das rendas dos clientes é {distancia_renda:.2f}")
print(f"O desvio padrão das rendas dos clientes é {desvio_padrao_renda:.2f}")
print(f"O coeficiente de variação das rendas dos clientes é {coeficiente_var_renda:.2f}")
print(f"A variancia das rendas dos clientes é {variancia_emprestado:.2f}")
print(f"A distancia da variância X média das rendas dos clientes é {distancia_emprestado:.2f}")
print(f"O desvio padrão das rendas dos clientes é {desvio_emprestado:.2f}")
print(f"O coeficiente de variação das rendas dos clientes é {coeficiente_emprestado:.2f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_financeira_renda_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_renda_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_financeira_renda_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_renda_outliers_superiores)

# Exibindo os dados sobre o valor emprestado
print('\nOBTENDO INFORMAÇÕES SOBRE EMPRÉSTIMO')
print('Medidas de Tendência Central')
print(f"\nA média dos empréstimos dos clientes é R$ {media_Vlr_emprestado:.2f}")
print(f"A mediana dos empréstimos dos clientes é R$ {mediana_Vlr_emprestado:.2f}")
print(f"A distância entre a média e a mediana dos empréstimos dos clientes é {distancia_Vlr_emprestado:.2f} %")
print(f"O maior valor dos empréstimos dos clientes é R$ {maior_Vlr_emprestado:.2f}")
print(f"O menor valor dos empréstimos dos clientes é R$ {menor_Vlr_emprestado:.2f}")
print(f"A amplitude dos empréstimos dos clientes é R$ {amplitude_Vlr_emprestado:.2f}")
print(f"O valor do q1 - 25% do empréstimo é R$ {q1_Vlr_emprestado:.2f}")
print(f"O valor do q2 - 50% da empréstimo é R$ {q2_Vlr_emprestado:.2f}")
print(f"O valor do q3 - 75% da empréstimo é R$ {q3_Vlr_emprestado:.2f}")
print(f"O valor do iqr = q3 - q1 da empréstimo é R$ {iqr_Vlr_emprestado:.2f}")
print(f"O limite inferior da empréstimo é R$ {limite_inferior_Vlr_emprestado:.2f}")
print(f"O limite superior da empréstimo é R$ {limite_superior_Vlr_emprestado:.2f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_financeira_Vlr_emprestado_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_Vlr_emprestado_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_financeira_Vlr_emprestado_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_Vlr_emprestado_outliers_superiores)

#Vizualizando os dados sobre 
print("\nVisualisando os dados...")
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('analise dos dados sobre renda X Emprestimo')

# posição 01: Gráfico das rendas
plt.subplot(2,2,1)
plt.title('Lista das rendas dor Cliente')
plt.bar(df_financeira['Id_cliente'],df_financeira['Renda'])

# posição 02: Gráfico dos emprestimos
plt.subplot(2,2,2)
plt.title('Lista de emprestimos')
plt.bar(df_financeira['Id_cliente'],df_financeira['Vlr_emprestado'])

# posição 03: Medidas descritivas
plt.subplot(2,2,3)
plt.text(0.1,0.9,f'Média das Rendas{media_renda}', fontsize=12)
plt.text(0.1,0.8,f'Mediana das Rendas{mediana_renda}', fontsize=12)
plt.text(0.1,0.7,f'Distância entre média e mediana das Rendas{distancia_renda}', fontsize=12)
plt.text(0.1,0.6,f'Maior valor {maior_renda}', fontsize=12)
plt.text(0.1,0.5,f'Menor valor {menor_renda}', fontsize=12)
plt.text(0.1,0.4,f'distancia entre variância e média{distancia_renda}', fontsize=12)
plt.text(0.1,0.3,f'Coeficiênte de variação {coeficiente_var_renda}', fontsize=12)


# posição 04: Medidas descritivas
plt.subplot(2,2,4)
plt.text(0.1,0.9,f'Média dos valores emprestados {media_Vlr_emprestado}', fontsize=12)
plt.text(0.1,0.8,f'Mediana dos valores emprestados {mediana_Vlr_emprestado}', fontsize=12)
plt.text(0.1,0.7,f'Distância entre média e mediana dos valores emprestados {distancia_Vlr_emprestado}', fontsize=12)
plt.text(0.1,0.6,f'Maior valor emprestado {maior_Vlr_emprestado}', fontsize=12)
plt.text(0.1,0.5,f'Menor valor emprestado {menor_Vlr_emprestado}', fontsize=12)
plt.text(0.1,0.4,f'distancia entre variância e média dos valores emprestados{distancia_Vlr_emprestado}', fontsize=12)
plt.text(0.1,0.3,f'Coeficiênte de variação dos valores emprestados {coeficiente_emprestado}', fontsize=12)

#exibindo o painel
plt.show()

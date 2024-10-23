import pandas as pd

dados = 'BASES\Funcionarios.csv'

df_funcionarios = pd.read_csv(dados, sep=',', encoding='iso-8859-1')

print("----- Dados financeiros ----")
print(df_funcionarios.head())

media_salaria = df_funcionarios['Salário'].mean(axis=0)
media_idade = df_funcionarios['Idade'].mean(axis=0)
menor_tempo = df_funcionarios['Tempo'].min(axis=0)
maior_tempo = df_funcionarios['Tempo'].max(axis=0)
diferenca_tempo = maior_tempo-menor_tempo
media_tempo_casa = df_funcionarios['Tempo'].mean(axis=0)
mais_novo = df_funcionarios['Idade'].min(axis=0)
mais_velho = df_funcionarios['Idade'].max(axis=0)
diferenca_idade = mais_velho-mais_novo
total_funcionarios = df_funcionarios['Nome'].count()
maior_salario = df_funcionarios['Nome'].max(axis=0)
menor_salario = df_funcionarios['Nome'].min(axis=0)


print("\n---- Informações Solicitadas ----")
print(f"A Média salarial é de: {media_salaria:.2f}")
print(f"A Média da idade é de: {media_idade:.0f}")
print(f"O funcionário com mais tempo de casa é: {maior_tempo}")
print(f"O funcionário com menor tempo de casa é: {menor_tempo}")
print(f"A diferença de idade entre eles é de: {diferenca_idade}")
print(f"A média de tempo de casa é de: {media_tempo_casa:.2f}")
print(f"O funcionnário mais novo é: {mais_novo}")
print(f"O funcionário mais velho é: {mais_velho}")
print(f"A quantidade de funcionarios é de: {total_funcionarios}")
print(f"O funcionario com maior salário é: {maior_salario}")
print(f"O funcionário com menor salário é: {menor_salario}")
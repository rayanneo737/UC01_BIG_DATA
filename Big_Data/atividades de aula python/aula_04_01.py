#criando a tabela alunos
import pandas as pd

Alunos = [
    ['João', 18,100],
    ['Maria', 15,80],
    ['Antônia', 18,100],
    ['Erica', 28,60],
    ['Pedro', 16,10]
]
#criando a coluna da tabela alunos
colunas = ['Nome','Idade','Média']

#criando o dataframe
df_alunos = pd.DataFrame(Alunos,columns = colunas)

#Exibindo os Dados 
print(df_alunos)

soma_idade = df_alunos['Idade'].sum(axis=0)
media_idade = df_alunos['Idade'].mean(axis=0)
maior_idade = df_alunos['Idade'].max(axis=0)
menor_idade = df_alunos['Idade'].min(axis=0)
maior_nome = df_alunos[df_alunos['Idade'] == maior_idade]['Nome']
menor_nome = df_alunos[df_alunos['Idade'] == menor_idade]['Nome']
#Realizando os calculos das médias

soma_media = df_alunos['Média'].sum(axis=0)
media_media = df_alunos['Média'].mean(axis=0)
maior_media = df_alunos['Média'].max(axis=0)
menor_media = df_alunos['Média'].min(axis=0)
maior_media_nome = df_alunos[df_alunos['Média'] == maior_media]['Nome']
menor_media_nome = df_alunos[df_alunos['Média'] == menor_media]['Nome']

print("\n-- Informações sobre as Idades dos alunos --")
print(f"A soma das idades é {soma_idade} anos.")
print(f"A média das idades é {media_idade:.0f} anos.")
print(f"A maior idade é {maior_idade} anos.")
print(f"A menor idade é {menor_idade} anos.")
print(f"O nome do aluno mais velho é {maior_nome.values[0]}")
print(f"O nome do aluno mais novo é {menor_nome.values[0]}")

# Exibindo os Cálculos das Médias
print("\n-- Informações sobre as Médias dos alunos --")
print(f"A soma das médias é {soma_idade:.1f}")
print(f"A Média das médias é {media_media:.1f}")
print(f"A maior média é {maior_media:.1f}")
print(f"A menor média é {menor_media:.1f}")
print(f"O nome do aluno com maior média é {maior_media_nome.values[0]}")
print(f"O nome do aluno com menor média é {menor_media_nome.values[0]}")
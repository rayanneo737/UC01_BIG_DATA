# Calcular a idade de uma pessoa a partir do ano de nascimento
import datetime
data_atual = datetime.date.today()
ano_atual = data_atual.year
nome = input("Informe o seu Nome: ")
ano_nasc = int(input("Informe o Ano de Nacimento: "))
idade = ano_atual - ano_nasc
print("Sr(a) ", nome, "a sua idade é: ",idade," anos.")
import datetime

dataAtual = datetime.date.today ()
name = input("Informe o seu nome: ")
anoNasc = int(input("Informe o ano do seu nascimento: "))

idade = dataAtual.year - anoNasc


print ("Sr(a)", name, "a sua idade é: ",idade,"Anos.")
prestacao = float(input("Informe o valor da prestação: "))
taxa = float(input("Informe a taxa: "))
tempo = int(input("Quantos meses tem de atraso: "))

valorFinal = prestacao + (prestacao*(taxa/100)*tempo)

print (valorFinal)
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso: "))
dormir = int(input("Informe quanto tempo você dormiu nas últimas 24h: "))

if (idade >= 16 and idade < 69) and (peso < 50) and (dormir < 6):
    print("Você pode doar sangue")

else:
    print("Você não pode doar sangue")
try:
    Nome = input("Digite seu nome: ")
    Idade = int(input("Qual idade você tem: "))
    Empresa = int(input("Quantos ano você tem de empresa: "))
except ValueError:
    print("Verifique os valores informados!")

else:
    
    if Idade >= 65:
        print("Você está apto!")
    elif Empresa >= 30:
        print("Você está apto!")
    elif Idade > 60 and Empresa >= 25:
        print("Você está apto!")   

    else:
        print("você está inapto!")      
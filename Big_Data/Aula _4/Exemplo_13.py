try:                                                            #Tratamento de erros
    num1 = int(input("Informe o primeiro numero: "))
    num2 = int(input("Informe o segundo numero: "))
except ValueError:
    print("Não é possível colocar letras na entrada de dados.")    
else:
    try:
        Calculo = num1 / num2
    except ZeroDivisionError:
        print("Não é possível dividir por zero.")
    else:
        print ("O calculo da sua divisão é: ",Calculo)
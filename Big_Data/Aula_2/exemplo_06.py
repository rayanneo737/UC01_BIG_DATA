h = float(input("Informe sua altura: "))
sexo = input("Informe M - para Masculino e F - para Feminino: ")
if sexo == "M" or sexo == "m":
    m = (72.7*h) - 58
    print(f"O seu peso ideal é {m:.2f}")
elif sexo == "F" or sexo == "f":
    f = (62.1 * h) - 44.7
    print(f"O seu peso ideal é {f:.2f}")
else:
    print("Verifique o Sexo Informado")
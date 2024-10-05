somaM = 0
somaF = 0
contM = 0
contF = 0
maior = 0
#maior = 0
for i in range(5):
    nome = input("Informe o nome: ")
    sexo = input("Informe o sexo: ")
    idade = int(input("informe sua idade: "))
    if idade > maior:
        maior = idade
    if sexo == "M" or sexo == "m":
        somaM = somaM + idade
        contM += 1
    if sexo == "F" or sexo == "f":
        somaF = somaF + idade
        contF += 1
media_m = somaM / contM
media_f = somaF / contF
print(f"A Soma das idades dos homens é {somaM}")
print(f"A soma das idades das mulheres é{somaF}")
print(f"A média das idades dos homens é {media_f:.0f}")
print(f"A média das idades das mulheres é {media_f:.0f}")
print(f"A soma das idades é {maior}")        

    

    

    

    
    


#separar a soma e a media pelo sexo da pessoa 
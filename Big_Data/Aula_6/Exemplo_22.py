nomes = []
medias = []
resp = "S"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do estudante: "))
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja continuar (S/N)? ")

for i in range(len(medias)):
    print(i, " - ", nomes[i], " - ", medias[i])

maior_media = max(medias)
pos = medias.index(maior_media)    

print(f"{nomes[pos]}, Você possui a maior média.")
print(f"A Maior média é de: {max(medias)}")                               #Maior média
print(f"A Menor média é de: {min(medias)}")                               #Menor média
print(f"A média da turma é: {(sum(medias)/len(medias)):.1f}")             #média da turma
print(f"A variação da maior para menor é: {min(medias)} menor - {max(medias)} maior")

medias.sort()


    

idades = [20,10,15,30,50,12,60,22,55,35]
print(f"A soma das idades é: {sum(idades)} anos.")
print(f"A Maior das idades é: {max(idades)} anos.")
print(f"A menor das idades é: {min(idades)} anos.")
print(f"A média das idades é: {sum(idades)/len(idades)} anos.")

idade = 1

for i in range(len(idades)):
    print(f"{idade} - {idades[i]}")
    idade += 1
    
idades.sort()
print(idades)
print(idades.sort())
idade = int(input("Informe a idade: "))
if idade < 18:
    print("Você é menor de idade")

elif idade == 18:
    print("Quase lá")  

elif idade > 65:
    print("Você tem que parar de beber")          

else: 
    print("Acesso liberado")

#Abaixo esta a contrução do mesmo codigo porém com adequação, está com '#' (Usando o conectivo And)
    
#idade = int(input("Informe a idade: "))
#if idade < 18:
#    print("Você é menor de idade")
#
#elif idade == 18:
#    print("Quase lá")  
#
#elif idade < 18 and idade > 65:
#    print("Você tem que parar de beber")          
#
#else: 
#    print("Acesso liberado")
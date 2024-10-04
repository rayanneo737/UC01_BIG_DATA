try:
    produto = input("Informe o nome do produto: ")
    quantidade = int(input("Informe a quantidade adquirida: "))
    preco = float(input("Informe o preço unitário: "))

except ValueError:
    print("Não é possível colocar letras nos preços ou quantidades!")

else:    
    Total = quantidade*preco
    print(f"O valor total sem desconto é R$ {Total:.2f}")

    if (quantidade <= 5):
        print("Seu desconto será de 2%: ",(Total*0.98))

    elif (quantidade > 5 and quantidade <=10):
        print("seu desconto será de 3%: ",(Total*0.97))

    else:
        print("Seu desconto será de 5% ",(Total*0.95))
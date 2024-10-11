usuarios  = ["Alessandro", "Rayanne","Isadora","Deise","Leticia"]
senha_1 = ["123", "456" , "789" , "243" , "853"]
usuario_1 = input("Informe seu nome: ")

for i in range(len(usuarios)):
    if usuarios [i] == usuario_1:
        senha = input("Informe a senha de acesso: ")
        if senha_1[i] == senha:
            resp = "Acesso liberado!"
        else:
            resp = "senha não confere!"    
        break
    
    else:
        resp = "Usuário não encontrado"
print(resp)



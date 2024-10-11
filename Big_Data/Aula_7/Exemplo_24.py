Temperatura = []
resp = "s"
while resp == "s" or resp == "S":
    Temperatura.append(float(input("informe a temperatura: ")))
    resp = input("Deseja continuar(S/N)")
print(f"A menor temperatura registrada foi {min(Temperatura)} ºC")    
print(f"A maior temperatura registrada foi {max(Temperatura)} ºC")
print(f"A temperatura média registrada foi {(sum(Temperatura)/len(Temperatura)):.1f} ºC")



import pandas as pd
def formatar(valor):
    return "{:.2f}%".format(valor)
Vacinas = pd.Series ([30000000, 25000000, 10000000, 5000000])
população = pd.Series ([213317639, 214477744, 215574303, 216687971])
taxa_vac = pd.Series((Vacinas / população)*100).apply(formatar)
print("----------- Dados da vacinação ----------------")
print(f"O total de vacinados {Vacinas.sum()}")
print(f"Média dos vacinados {Vacinas.mean():.0f}")
print("\n-----------Dados da população----------------")
print(f"O total de vacinados {população.sum()}")
print(f"Total da população {população.mean():.0f}")
print("\n-----------Taxa de vacinação-----------------")
print(f"{taxa_vac}")
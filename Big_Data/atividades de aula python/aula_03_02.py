import pandas as pd
roubo = pd.Series ([100,90,80,120,110,90,70])
furtos = pd.Series ([80,60,70,60,100,50,30])
recu_auto = pd.Series([70,50,90,80,100,70,50])
roubo_furto = roubo + furtos
tx_recuperacao = ((recu_auto / roubo_furto)*100).apply(format)
print("\n- total geral de roubos - ")
print(f"{roubo_furto.sum()}")
print("\n- Total de roubos diários - ")
print(f"{roubo_furto}")
print("\n- Taxa de Recuperação diária - ")
print(f"{tx_recuperacao}")
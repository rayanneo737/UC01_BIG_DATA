import pandas as pd
maria = pd.Series ([800,700,1000,900,1200,600,600])
joão = pd.Series ([900,500,1100,1000,900,500,700])
miguel = pd.Series([700,600,900,1200,900,700,400])
print(f"A média do valor vendido:\n de Maria {maria.mean():.1f}\n de João: {joão.mean():.1f}\n de Miguel: {miguel.mean():.1f}")
print(f"O maior valor vendido:\n de Maria {maria.max():.1f}\n de João: {joão.max():.1f}\n de Miguel: {miguel.max():.1f}")
print(f"O menor valor vendido:\n de Maria {maria.min():.1f}\n de João: {joão.min():.1f}\n de Miguel: {miguel.min():.1f}")
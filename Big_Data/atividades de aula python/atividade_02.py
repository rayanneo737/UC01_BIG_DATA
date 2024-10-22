import pandas as pd
max = pd.Series([42,38,34,33,29,27,36])
mix = pd.Series([14,16,17,19,22,18,20])
print("A amplitude da Máxima temperatura com a menor é de: ", (max-mix))
media1 = (42+38+34+33+29+27+36)/7 
# ou media1 = media1.mean() -- calcula a média automaticamente
# ou media2 = media2.mean() -- calcula a média automaticamente
print(f"A temperatura média da máxima é de: {media1:.1f}")
media2 = (14+16+17+19+22+18+20)/7
print(f"A temperatura média da minima é de: {media2:.1f}")
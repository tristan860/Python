# massiivid - array
# 28.11.2023
# Tristan Jugapuu

"""
Õpilased
Loo õpilaste nimedest loend. Programm lubab loendis olevaid nimesid muuta.
"""

opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
jrk = 1
for opilane in opilased:
    print(f"{jrk}. {opilane}")
    jrk += 1
valik = int(input("mitmendat nime tahad muuta: "))
uusnimi = input("Lisa uus nimi: ")
del opilased[valik-1]
opilased.insert(valik-1, uusnimi)

print(opilased)
    

"""
Nimede lisamine loendisse
Küsi kasutajalt viis nime. 
Salvesta need loendisse ja kuva tähestikulises järjekorras. 
Kuva eraldi viimati lisatud nimi
"""

nimed = []

for i in range(5):
    nimi = input("lisa nimi: ")
    nimed.append(nimi)
print("viimati lisatud nimi: ", nimed[-1])
nimed.sort()

print(nimed)


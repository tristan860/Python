# Tristan Jugapuu
# 16.01.2024
# Iseseisevtöö 5
import random

# Ülesanne 13

try:
    paaris_või_paaritu = input("Sisesta arv: ")
    if paaris_või_paaritu == "" or paaris_või_paaritu == 0:
        print("vale sisend")
    elif int(paaris_või_paaritu) % 2 == 0:
        print("Arv on paaris")
    else:
        print("Arv on paaritu")
except ValueError:
    print("vale sisend")
    

# Ülesanne 1

def korrutamine(arv1, arv2):
    vastus = int(input(f"{arv1} * {arv2} = "))
    if vastus == arv1 * arv2:
        print("Õige vastus!")
    else:
        print("Vale vastus!")
        print(f"Õige vastus on {arv1 * arv2}")

for i in range(10):
    arv1 = random.randint(1,50)
    arv2 = random.randint(1,50)
    korrutamine(arv1, arv2)

# Ülesanne 3
    
positiivsed = []
negatiivsed = []
for i in range(5):
    arv = int(input("Sisesta arv: "))
    if arv > 0:
        positiivsed.append(arv)
    elif arv < 0:
        negatiivsed.append(arv)
    else:
        print

print(f"Positiivsed arvud: {positiivsed}")
print(f"Negatiivsed arvud: {negatiivsed}")

# Ülesanne 5

shopping_list = []
while True:
    item = input("Sisesta toode: ")
    if item == "":
        break
    else:
        shopping_list.append(item)
print(shopping_list)

# Ülesanne 7

#Küsib kasutajalt kalkulaatori valiku
kalkulaatori_valik = input("Vali kalkulaator: 1 - Eurokalkulaator, 2 - Eestikroonikalkulaator: ")

#Valib kalkulaatori
if kalkulaatori_valik == "1":
    Eurokalkulaator = ()
#Küsib kasutajalt eurode summa
    euro = float(input("Sisesta eurode summa: "))
#Arvutab eurod Eesti kroonideks    
    Eesti_kroon = euro * 15.6466
    print(f"{euro} eurot on {Eesti_kroon} Eesti krooni")
elif kalkulaatori_valik == "2":
    Eestikroonikalkulaator = ()
#Küsib kasutajalt Eesti kroonide summa
    Eesti_kroon = float(input("Sisesta Eesti kroonide summa: "))
#Arvutab Eesti kroonid eurodeks
    euro = Eesti_kroon / 15.6466
    print(f"{Eesti_kroon} Eesti krooni on {euro} eurot")
else:
#Kui kasutaja valib vale kalkulaatori, siis programm ütleb, et valik on vale
    print("Vale valik!")

# Ülesanne 9

#Küsib kasutajalt emaili
Emaili_kontroll = input("Sisesta email kujul eesnimi.perenimi@server.com: ")

#Kontrollib kas email on õigesti sisestatud ja prindib vastuse
if "@" in Emaili_kontroll:
    print("tere tulemast, " + Emaili_kontroll.split("@")[0].split(".")[0].capitalize() +","+ "sinu email on server serveris ja domeeniks on com")
else:
    print("Email on valesti sisestatud")

# Ülesanne 11

#Küsib kasutajalt salakeele loomise või salakeele tõlkimise
tõlkimine = input("valige kas: 1- salakeele loomine või 2- salakeele tõlkimine: ")

#Kui kasutaja valib salakeele loomise, siis programm küsib kasutajalt teksti ja asendab selle salakeelega
if tõlkimine == "1":
    salakeel = ()
    tekst = input("Sisesta tekst: ").lower()
    salakeel = (tekst.replace("a", "e").replace("o", "u").replace("i", "o").replace("e", "i").replace("u", "a"))
    print(salakeel)
#Kui kasutaja valib salakeele tõlkimise, siis programm küsib kasutajalt teksti ja asendab selle salakeelest arusaadavaks
elif tõlkimine == "2":
    salakeel = ()
    tekst = input("Sisesta tekst: ").lower()
    salakeel = (tekst.replace("e", "a").replace("u", "o").replace("o", "i").replace("i", "e").replace("a", "u"))
    print(salakeel)
else:
    print("Vale valik!")


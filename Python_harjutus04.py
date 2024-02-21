import random
# Tristan Jugapuu
# 21.11.2023
# Ülesanne 4

#Ruutude ja kuupide tabel
print("Arv Ruut Kuup")
for i in range(1,11):
    print(f"{i} {i**2:4} {i**3:5}")

input()


#pank
raha = 10000
aasta = 5
konto = raha
intress = 0.05

print("Aasta   Algsumma    Intress     Aasta lõpuks")
for i in range(aasta):
    print(f"{i+1} {konto:>14.2f} {konto * intress:>9.2f} {konto+konto*intress:>13.2f}")
    konto = konto + konto * intress

print(f"Summa kokku : {konto:.2f}€")
print(f"Kasum : {konto-raha:.2f}€")

input()


#arvamismäng while&for
loop = 1
voidud = 0

while loop == 1:
    print("------------ ARVAMISE MÄNG ------------")
    suv = random.randint(1,10)
    #print(suv)
    for i in range(3):
        arva = int(input("Paku arv 1-10: "))
        if suv == arva:
            print("Arvasid ära")
            voidud= voidud+1
            break
        else:
            print("Proovi veel!")
    print("------------ GAME OVER ------------")
    print(f"voidud = {voidud}")
    jatka = input("Soovid jätkata? y/n: ")
    if jatka == "n":
        loop = 0


#viisikud
for i in range(1,101):
    if i%5 == 0:
        print(i)


#Korrutustabel
for j in range (1,11):
    for i in range(1,11):
        print(f"{j} * {i} = {j*i}")


#paaris ja paaritu
for i in range(1,10+1):
    if i % 2 == 0:
        v = "paaris"
    else:
        v = "paaritu"
    print(i,v)

    


#loto
for x in range(5):
    print(random.randint(0,9),end="")


print()
"""
Tärnid
Loo tsükkel, mis väljastab 5×5 tärnid
Loo tsükkel, mis väljastab tärnidest kasvava kolmnurga
Loo tsükkel, mis väljastab tärnidest kahaneva kolmnurga
"""
j = 5
for i in range(j):
    print("*"*(i+1))
j = 5
for i in range(5):
    print("*"*j)
    j = j - 1
print()
j = 5
for i in range(5):
    print("*"*j)

"""
Jalgpalli meeskond
Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita.
"""

sugu = "m"
if sugu == "m":
    vanus = 17
    if vanus >= 16 and vanus <= 18:
        print("Tere tulemast")
    else:
        print("Vanus ei sobi")
else:
    print("ei pääse meeskonda")

"""
Müük
Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
Kuva toote lõplik hind. Plokkskeemi pole vaja!
"""

hind = 10
if hind <= 10:
    vastus = 0.1
else:
    vastus = 0.2
print(f"hind on {hind-hind*vastus} €")

"""
Juubel
Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
Plokkskeemi pole vaja!
"""

v = int(input("Sisesta sünnipäev: "))
if v % 5 == 0:
    vastus = "on"
else:
    vastus = "ei ole"
print(f"vanus {v}: {vastus} juubel")

"""
Matemaatika
Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""

nr1 = int(input("Arv 1: "))
nr2 = int(input("Arv 2: "))
tehe = input("Vali tehe + - * /: ")

if tehe == "+":
    vastus = nr1 + nr2
elif tehe == "-":
    vastus = nr1 - nr2
elif tehe == "*":
    vastus = nr1 * nr2
elif tehe == "/":
    vastus = round(nr1 / nr2, 2)
else:
    vastus = "ära pulli mees!"

print(f"{nr1} {tehe} {nr2} {vastus}")

"""
Ruut
Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.
"""

nr1 = int(input("Ruudu 1. külg: "))
nr2 = int(input("Ruudu 2. külg: "))

if nr1 == nr2:
    print("Juhuu ruut")
else:
    print("Mingi muu asi")
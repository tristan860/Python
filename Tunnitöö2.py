# Tristan Jugapuu
# 18.12.2023
import random

# äratus

def aratus(nr):
    for i in range(nr):
        print("tõuse ja sära!")


# Jänesevanemad

def porgandid(r):
    joostud_ringid = 0
    porgandid = 0
    while joostud_ringid < r:
        joostud_ringid+=1
        if joostud_ringid%2==0:
            porgandid+=joostud_ringid

    print(f"Jänkukesekene saab: {porgandid}, porgandit!")


# Täringud
    
def taringud(arv):
    for i in range(arv):
        print(random.randint(1,6))


# Male

def Male(ruutude_arv):
    ruut = 1
    nisuterad = 1
    while ruut <ruutude_arv:
        nisuterad = nisuterad*2
        ruut+=1
    print(f"Nisuteri {ruut}. ruudu eest: {nisuterad}")

# Õunad

def lumivalgeke(p):
    ounad = 14
    for i in range(p):
        pounad = random.randint(1,2)
        ounad -= pounad
        print(pounad)
    print(f"Lumivalgekesele jäi {ounad} õuna")

kordus = int(input("Sisestage mitu korda äratada: "))
aratus(kordus)
ringid = int(input("mitu ringi: "))
porgandid(ringid)
arv = int(input("sisesta täringute arv: "))
taringud(arv)
taisarv = int(input("sisesta täisarv: "))
Male(taisarv)
mitu_ouna = int(input("Mitu pöialpoissi tahab õunu? "))
lumivalgeke(mitu_ouna)
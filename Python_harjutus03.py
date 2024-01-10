# Tristan Jugapuu
# 21.11.2023
# Ülesanne 3

"""
Palindroom
"""
tekst = input("Sisesta tekst: ")
print(tekst == tekst[::-1])


"""
Tundide ajad
Kasutaja sisestab tundide alguse ja lõpu. Näiteks 8:30 ja 14:15
Sinu programm leiab, kui pikk oli õpilase päev
Väljasta täislause ja kasuta vormindamisel format() meetodit.
"""
algus = input("tundide algus: ")
lõpp = input("tundide lõpp: ")

hh1,mm1 = algus.split(":")
hh2,mm2 = lõpp.split(":")

algus_minutid = int(hh1) * 60 + int(mm1)
loppu_minutid = int(hh2) * 60 + int(mm2)

ajavahe = loppu_minutid - algus_minutid
tunnid = ajavahe // 60
minutid = ajavahe % 60

print(f"{tunnid}:{minutid}")


"""
Email
Küsi kasutajalt emaili ja kontrolli, kas see sisaldas @-märki.
Näiteks: sisend–>minu@mail.ee; väljund–> True või False
"""
ask = input("Sisesta Email: ")
print('@' in ask)			#true



"""
Vandumine
Kui kasutaja sisestab “kogemata” teksti, kus leidub sõna ‘kurat’, siis sinu programm asendab need tärnidega.
Näiteks: sisend–>Kurat küll!; väljund–>*** küll!
"""
ask = input("Sisesta tekst: ")
print(f"{ask.replace('kurat', '***')}!")

ask = input("Sisesta nimi: ")
print(f"Tere {ask.strip().capitalize()}!")

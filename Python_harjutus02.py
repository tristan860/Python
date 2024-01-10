import math
import turtle
# Tristan Jugapuu
# 14.11.2023
# Ülesanne 2


"""
Kilpkonn - 	küsib kasutajalt ringi raadiust
            kasutab funktsiooni ringi joonistamiseks
"""
w = turtle.Screen()

def ring(r):
    krokodill = turtle.Turtle()
    krokodill.circle(r)
   
r = w.numinput("ringi loomine","Sisesta ringi raadius")

print(r)
ring(r)


liitrid = int(input("Sisesta tangitud liitrite arv: "))
km = int(input("Sisesta läbitud kilomeetrid: "))
kytusekulu = liitrid /( km / 100)
print(kytusekulu)


arv = int(input("Sisesta arv: "))
bii = bin(arv)
heks = hex(arv)
print(bii, heks)


minutid = int(input("Sisesta aeg minutites: "))
ükstund = 60
tunnid = (minutid//ükstund)
üleminutid =(minutid % ükstund)
print (str(tunnid),":",str(üleminutid) ,)


külg_a = 16
külg_b = 9
Pythagoraseteoreem =round((külg_a*külg_a+külg_b*külg_b),2)
print("Kolmnurga hüpotenuus on",str(Pythagoraseteoreem),)


kiirus = 29.9
tund = 60
aeg = 24
kaugus = round((kiirus/tund)*aeg, 2)
print("Rulluisutaja jõudis 24 minutiga",str(kaugus),"km kaugusele")


pitsahind = 12.90
jootraha = 0.1
maksjad = 3
maksta = (pitsahind+pitsahind*jootraha)/maksjad
print("igaüks peab maksma",str(maksta),)


hind = 36.75
ale = 0.4
kogus = 3
summa = round((hind-hind*ale)*kogus,2)
print( "kolme toote hind kokku on" +str(summa))


a, b, c = 7,7,7
p = a + b + c
print("kolmnurga ümbermõõt on",p,"cm")

turtle.exitonclick()


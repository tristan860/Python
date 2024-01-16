# Tristan Jugapuu
# 10.01.2024
# Iseseisevtöö 4

def banner(t):
    print(t.upper())

ask = int(input("Mitu korda?:  "))
ask2 = input("Reklaamlause:  ")

for i in range(ask):
    print(ask2)

def mahlapakkidearv(kg):
    pakid = round(kg * 0.4 / 3)
    return pakid

kogus = float(input("õunte kogus: "))
print(mahlapakkidearv(kogus))

def eelarve(kylalised):
    summa = kylalised * 10 + 55
    return summa

palju = int(input("külaliste arv: "))
palju2 = int(input("mitu tuleb: "))
print(f"Maksimaalne eelarve: {eelarve(palju)}€")
print(f"Minimaalne eelarve: {eelarve(palju2)}€")

külalised = 3
def tervitus(n):
    print('võõrustaja: "Tere,"!')
    print(f"Täna {n}. kord tervitada!")
    print(f'külaline: "Tere, suur tänu kutse eest!"')

for i in range(külalised):
    tervitus(i+1)


def pronksikarva_summa(f):
    kassa = 0   
    fail = open("mündid.txt")
    for mynt in fail:
        if int(mynt) < 10:
            print(mynt, end="")
            kassa += int(mynt)
    print("Kassa: ", kassa)
    
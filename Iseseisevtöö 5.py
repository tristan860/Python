# Tristan Jugapuu
# 16.01.2024
# Iseseisevtöö 5
import random

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


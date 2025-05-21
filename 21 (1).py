#Kapitány Levente Csaba

import random

p1Re = random.randint(2, 11)
p2Re = random.randint(2, 11)

p1Rm = random.randint(2, 11)
p2Rm = random.randint(2, 11)

p1Rh = random.randint(2, 11)
p2Rh = random.randint(2, 11)

p1Rg = random.randint(2, 11)
p2Rg = random.randint(2, 11)


ertek = []
masErtekek = []

ertek.append(p1Re+p1Rm)

print("Hány játékos szeretne játszani?")
jatek = input("Egy vagy kettő játékos:")

if jatek == "Egy":
    print("Egy játékos mód!")
    print(f"Kezdjük is a játékot a kártyáid {ertek}!")
    keres = input("Kérsz még egy lapot?")
    if keres == "Igen":
        ertek.append(p1Rh)
        osszeg = sum(ertek)
        print(f"Az új kártyával eggyütt {osszeg} lapod van!")
    else:
        osszeg2 = sum(ertek)
        print(f"Nem kértél többet! Jelenlegi lapjaid összege {osszeg2}")


elif jatek == "Kettő":
    print("Két játékos mód!")
    print("Adjátok meg a felhasználó neveteket!")
    j1 = input("Első játékos neve:")
    j2 = input("Második játékos neve:")
    print(f"Kezdjük is a játékot a kártyáid {j1}: {p1Re + p1Rm} és {j2}: {p2Re + p2Rm}!")
    val1 = input(f"{j1} kérsz még egy lapot?")
    if val1 == "igen":
        jpu1 = random.randint(2, 11)
        print(f"Kértél még egy lapot! A kártya! {jpu1}")
        print(f"A kártyáid összege:{p1Re + p1Rm + jpu1 }")
    else:
        print(f"{j1} meg áltál ennyi kártyánál: {p1Re + p1Rm}")


else:
    print("Sajnos nem értem😥. Megismételnéd?")
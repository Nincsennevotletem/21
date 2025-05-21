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
        szamok1 = p2Re + p2Rm + jpu1
    else:
        print(f"{j1} meg áltál ennyi kártyánál: {p1Re + p1Rm}")

    val2 = input(f"{j2} Ez a te időd kérsz még egy lapot?")
    if val2 == "igen":
        jpu2 = random.randint(2, 11)
        print(f"Kértél még egy lapot! A kártya!{jpu2}")
        print(f"A lapjaid összege:{p2Re + p2Rm + jpu2}")
        szamok2 = p2Re + p2Rm + jpu2
    else:
        print(f"Nem kértél több lapot! A lapjaid összege mardt:{p2Re + p2Rm}")

    print(f"Összegzés!")
    print(f"A lapjaid értéke {j1}:{szamok1} A lapjaid értéke {j2}:{szamok2}")

    if szamok1 > 21:
        print(f"{j1} túl nayg a szám vesztettél!")
        print(f"Gartulálok {j2}")
    elif szamok2 > 21:
         print(f"{j2} túl nayg a szám vesztettél!")
         print(f"Gartulálok {j1}")
    else:
        print("Itt az ideje az eredmény hírdetésnek!")
        if szamok1 > szamok2:
            print(f"{j1} Gartulálok nyertél!")

        else:
            print(f"{j2} Gartulálok nyertél!")
        



else:
    print("Sajnos nem értem😥. Megismételnéd?")
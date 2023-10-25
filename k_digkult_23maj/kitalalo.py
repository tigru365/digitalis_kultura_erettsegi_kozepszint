import random

random.seed()

# 1. feladat
szavak = ("fuvola", "csirke", "adatok", "asztal", "fogoly",
          "bicska", "farkas", "almafa", "babona", "gerinc",
          "dervis", "bagoly", "ecetes", "angyal", "boglya")

# 2. feladat
rejtett_szo = random.choice(szavak)

# 3. feladat
stop = False
tippek_szama = 0
while not stop:
    valasz = input("Kérem a tippet: ")
    if valasz == "stop":
        stop = True
    else:
        tippek_szama += 1
        eredmeny = ""
        for betu_keresett, betu_megadott in zip(rejtett_szo, valasz):
            eredmeny += (betu_keresett if betu_keresett == betu_megadott else ".")
        print(f"Az eredmény: {eredmeny}\n")
        if eredmeny == rejtett_szo:
            break

# 4. feladat
if not stop:
    print(f"{tippek_szama} tippeléssel sikerült kitalálni.")

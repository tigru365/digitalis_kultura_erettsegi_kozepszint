""" Szállítás (2023.10.25)
"""

# 1. feladat
tomegek = [16, 8, 9, 4, 3, 2, 4, 7, 7, 12, 3, 5, 4, 3, 2]
# print(f"{tomegek = }")

## A tárgyak tömegének tárolása a szövegfájlból beolvasva
# from pathlib import Path
# fajl = Path.cwd() / "forras" / "tomeg.txt"
# with fajl.open(encoding="ascii") as forrasfajl:
#     tomegek = list(map(lambda x: int(x.strip()), forrasfajl.readline().split(",")))
# print(f"{tomegek = }")

# 2. feladat
print("2. feladat")

print(f"A tárgyak tömegének összege: {sum(tomegek)} kg\n")

# 3. feladat
print("3. feladat")

MAX_TOMEG = 20
doboz_tomeg = 0
dobozok = []

for tomeg in tomegek:
    if doboz_tomeg + tomeg > MAX_TOMEG:
        dobozok.append(doboz_tomeg)
        doboz_tomeg = tomeg
    else:
        doboz_tomeg += tomeg
dobozok.append(doboz_tomeg)

print(f"A dobozok tartalmának tömege (kg):", *dobozok)
print(f"A szükséges dobozok száma: {len(dobozok)}")

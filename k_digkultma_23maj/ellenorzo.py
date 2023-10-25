# 1. feladat
taj_szam = input("Kérem a TAJ-számot: ")
# taj_szam = "012345672"

# 2. feladat
ellenorzo_szam = int(taj_szam[-1])
print(f"Az ellenőrzőszámjegy: {ellenorzo_szam}")

# 3. feladat
osszeg = 0
for i, sz in enumerate(taj_szam[:-1]):
    szam = int(sz)
    if ((i + 1) % 2 != 0):
        osszeg += szam * 3
    else:
        osszeg += szam * 7
print(f"A szorzatok összege: {osszeg}")

# 4. feladat
if osszeg % 10 == ellenorzo_szam:
    print("Helyes a szám!")
else:
    print("Hibás a szám!")
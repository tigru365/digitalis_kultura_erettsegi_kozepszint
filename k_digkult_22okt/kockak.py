import random

# 1. feladat
beolvasas_ok = False
while not beolvasas_ok:
    try:
        dobasok_szama = int(input("Hány alkalommal legyen feldobás? "))
        if dobasok_szama < 1:
            raise ValueError
        beolvasas_ok = True
    except ValueError:
        print("Kérem, hogy pozitív egész számot adjon meg!")

# 2. feladat
random.seed()

dobasok = []
for _ in range(dobasok_szama):
    dobas = [random.randint(1, 6) for _ in range(3)]
    dobasok.append(dobas)

# 3. feladat
hanyszor_nyert = {'Anni': 0, 'Panni': 0}
for dobas in dobasok:
    osszeg = sum(dobas)
    print(f"Dobás: {dobas[0]} + {dobas[1]} + {dobas[2]} = {osszeg}", end="")
    if osszeg < 10:
        nyertes = "Anni"
    else:
        nyertes = "Panni"
    print(f"\t  Nyert: {nyertes}")

# 4. feladat
nyertesek = ["Anni" if sum(d) < 10 else "Panni" for d in dobasok]
print(f"A játék során {nyertesek.count('Anni')} alkalommal Anni, {nyertesek.count('Panni')} "
      + "alkalommal Panni nyert.")

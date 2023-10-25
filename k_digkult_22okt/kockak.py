import random

random.seed()

# 1. feladat
dobasok_szama = int(input("Hány alkalommal legyen feldobás? "))
# dobasok_szama = 5

# 2. feladat
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

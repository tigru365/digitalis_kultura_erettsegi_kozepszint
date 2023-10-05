# 1. feladat
parancs = input("Kérem a robot parancsait: ")

# 2. feladat
betuk = {'E': 0, 'D': 0, 'K': 0, 'N': 0}
for betu in parancs:
    betuk[betu] += 1

for irany, darab in betuk.items():
    print(f"{irany} betűk száma: {darab}")

# 3. feladat
v_irany = betuk['K'] - betuk['N']
f_irany = betuk['E'] - betuk['D']

uj_parancs = ""
if v_irany < 0:
    uj_parancs += ("N" * -v_irany)
else:
    uj_parancs += ("K" * v_irany)

if f_irany < 0:
    uj_parancs += ("D" * -f_irany)
else:
    uj_parancs += ("E" * f_irany)

print(f"Egy legrövidebb út parancsszava: {uj_parancs}")

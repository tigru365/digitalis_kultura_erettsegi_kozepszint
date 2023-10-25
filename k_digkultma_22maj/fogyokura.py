# 1. feladat
hetek_szama = int(input("Hetek száma="))
kivant_testtomeg = float(input("Elérni kívánt testtömeg (kg)="))
# hetek_szama = 6
# kivant_testtomeg = 93.5

# 2. feladat
heti_tomeg = []
for het in range(1, hetek_szama + 1):
    tomeg = float(input(f"{het}. héten="))
    heti_tomeg.append(tomeg)

# 3. feladat
het_elerte = 0
for i, tomeg in enumerate(heti_tomeg):
    if tomeg <= kivant_testtomeg:
        het_elerte = i + 1
        break

if het_elerte > 0:
    print(f"Mari néni a(z) {het_elerte}. héten érte el a célt.")
else:
    print("Sajnos Mari néni nem érte el a célját.")

# 4. feladat
szamlalo = 0
for i in range(len(heti_tomeg) - 1):
    if heti_tomeg[i + 1] > heti_tomeg[i]:
        szamlalo += 1

print(f"A tömege {szamlalo} esetben nőtt egyik hétről a másikra.")

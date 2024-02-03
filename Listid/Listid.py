#1

glas = list("aeiouõäöüAEIOUÕÄÖÜаеёиоуыэюяАЕЁИОУЫЭЮЯ")
sogl = list("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ")
sumbolid = list(",.!?;:-—–()[]{}\"'")
spaces=list(" ")
while True:
    sisend=str(input("Palun Sisestage sõna või lause /n>> "))
    
    space = 0
    g_arv = 0
    s_arv = 0
    sumb = 0
    
    for char in sisend:
        if char in glas:
            g_arv += 1
        elif char in sogl:
            s_arv += 1
        elif char in sumbolid:
            sumb += 1
        elif char in spaces:
            space += 1
        
    print(f"Vokaalid: {g_arv}")
    print(f"Konsonandid: {s_arv}")
    print(f"Sümbolid: {sumb}")
    print(f"Tühikud: {space}")


#2
import random
names = []
for i in range(5):
    while True:
        name = input("Sisestage nimi: ")
        if name not in names:
            names.append(name)
            break
        else:
            print("See nimi on juba sisestatud. Palun sisestage teine nimi.")
print(f"\nViimati sisestatud nimi: {names[-1]}")
names.sort()
ages = [random.randint(18, 80) for i in range(len(names))]
for i, name in enumerate(names):
    print(f"{name} - Vanus: {ages[i]} aastat")

max_age = max(ages)
min_age = min(ages)
total_age = sum(ages)
average_age = total_age/len(ages)

print("\nVanuste statistika:")
print("Suurim vanus:", max_age)
print("Väikseim vanus:", min_age)
print("Vanuste summa:", total_age)
print("Keskmine vanus:", average_age)

while True:
    change_name = input("\nKas soovite nimesid muuta? (y/n): ")
    if change_name.lower() == 'n':
        break
    elif change_name.lower() == 'y':
        change_name = input("\nSisestage nimi, mida soovite muuta: ")
        if change_name in names:
            index = names.index(change_name)
            new_name = input("Sisestage uus nimi: ")
            names[index] = new_name
            print("Nimi muudetud edukalt.")

            names.sort()
            print("\nUuendatud nimede ja vanuste nimekiri:")
            for i in range(len(names)):
                print(f"{names[i]} - Vanus: {ages[i]} aastat")

            print("\nVanuste statistika:")
            print("Suurim vanus:", max_age)
            print("Väikseim vanus:", min_age)
            print("Vanuste summa:", total_age)
            print("Keskmine vanus:", average_age)
        else:
            print("Sellist nime ei leitud. Palun sisestage olemasolev nimi.")
    else:
        exit(0)

    
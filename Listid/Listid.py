# import random
# from secrets import choice
# nimed=['mati', 'meelis', 'kati', 'mati', 'emma', 'nina']
# while True:
#     print("*************")
#     v=input("N-näitada andmeid\nL-lisada andmeid\nK-andmete kutsutamine\nH-andmete haldus\n")
#     if v=="N":
#         v=input("Kas juhuslik(J) nimi või terve loetelu(T)?")
#         if v=="T":
#             print(nimed)
#         elif v=="J":
#             print(choice(nimed))
#     elif v=="L":
#         v=input("Kas nimekirja lõppu(L) või positsioonile(P)?")
#         if v=="L":
#             nimi=input("Sisesta nimi: ")
#             nimed.append(nimi)
#         elif v=="P":
#             nimi=input("Sisesta nimi: ")
#             ind=int(input("Mis kohale: "))
#             nimed.insert(ind-1,nimi)
#     elif v=="K":
#         v=input("Kas nimi järgi(N) või indeksi järgi(I) või kõik nimed(K)?")
#         if v=="I":
#             v=int(input("Sisesta indeks: "))
#             nimed.pop(ind-1)
#         elif v=="N":
#             nimi=input("Sisesta nimi: ")
#             mitu=int(nimed.count(nimi))
#             if mitu>0:
#                 for i in range(mitu):
#                     nimed.remove(nimi)
#             else:
#                 print(f"{nimi} ei ole loetelus")
#         elif v=="K":
#             nimed.clear()
#     elif v=="H":
#         v=input("Sorteerimine(S), Kopeerimine(K) või Ümber pööramine(P)")
#         if v=="S":
#             v=int(input("A-Z(1) või Z-A (2)"))
#             if v==1:
#                 nimed.sort()
#             if v==2:
#                 nimed.sort(reverse=True)
#             print(nimed)
#         elif v=="K":
#             nimed.copy()
#             print(nimed)
#         elif v=="P":
#             nimed.reverse()
#             print(nimed)
#     elif v=="I":
#         v=input("Sisesta otsingut nimi: ")
#         d=nimed.count(v)
#         if d>1:
#             for i in range(d):
#                 print(nimed.index(v, i))
#         elif d==1:
#             print(nimed.index(v))
#         elif d==0:
#             print("ei ole nimi")
                

#﻿# #1

# glas = list("aeiouõäöüAEIOUÕÄÖÜаеёиоуыэюяАЕЁИОУЫЭЮЯ")
# sogl = list("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ")
# sumbolid = list(",.!?;:-—–()[]{}\"'")
# spaces=list(" ")
# while True:
#     sisend=str(input("Palun Sisestage sõna või lause /n>> "))
    
#     space = 0
#     g_arv = 0
#     s_arv = 0
#     sumb = 0
    
#     for char in sisend:
#         if char in glas:
#             g_arv += 1
#         elif char in sogl:
#             s_arv += 1
#         elif char in sumbolid:
#             sumb += 1
#         elif char in spaces:
#             space += 1
        
#     print(f"Vokaalid: {g_arv}")
#     print(f"Konsonandid: {s_arv}")
#     print(f"Sümbolid: {sumb}")
#     print(f"Tühikud: {space}")


##2
import random
names = []
for i in range(5):
    n=names[i]
    d=names.count(n)
    if d>1:
        for i in range(d-1):
            names.remove(n)
    print(names)
    # while True:
        # name = input("Sisestage nimi: ")
        # names.append(name)
        # break
        #if name not in names:
        #    names.append(name)
        #    break
        #else:
        #    print("See nimi on juba sisestatud. Palun sisestage teine nimi.")
#print(f"\nViimati sisestatud nimi: {names[-1]}")
#names.sort()
#ages = [random.randint(18, 30) for i in range(len(names))]
#for i, name in enumerate(names):
#    print(f"{name} - Vanus: {ages[i]} aastat")

#max_age = max(ages)
#min_age = min(ages)
#total_age = sum(ages)
#average_age = total_age/len(ages)

#print("\nVanuste statistika:")
#print("Suurim vanus:", max_age)
#print("Väikseim vanus:", min_age)
#print("Vanuste summa:", total_age)
#print("Keskmine vanus:", average_age)

#while True:
#    change_name = input("\nKas soovite nimesid muuta? (y/n): ")
#    if change_name.lower() == 'n':
#        break
#    elif change_name.lower() == 'y':
#        change_name = input("\nSisestage nimi, mida soovite muuta: ")
#        if change_name in names:
#            index = names.index(change_name)
#            new_name = input("Sisestage uus nimi: ")
#            if new_name not in names:
#                names[index] = new_name
#            else:
#                print("See nimi on juba sisestatud. Palun sisestage teine nimi.")
#                continue
            
#            names.sort()
#            print("\nUuendatud nimede ja vanuste nimekiri:")
#            for i in range(len(names)):
#                print(f"{names[i]} - Vanus: {ages[i]} aastat")
            
#            print("\nVanuste statistika:")
#            print("Suurim vanus:", max_age)
#            print("Väikseim vanus:", min_age)
#            print("Vanuste summa:", total_age)
#            print("Keskmine vanus:", average_age)
#        else:
#            print("Sellist nime ei leitud. Palun sisestage olemasolev nimi.")
#    else:
#        continue

##3 Tärnid

#arvud = [10, 11, 15, 20, 18, 10]


#for arv in arvud:
#    print('*' * arv)

##4
#while True:
#    index=input("Sisesta index: ")
#    if len(index) != 5 or not index.isdigit():
#        print("Vigane postiindeks! Palun sisestage 5 numbrist koosnev postiindeks.")
#        break
#    maakonna_number = int(index[0])
#    maakonnad = {
#        1: "Tallinn",
#        2: "Narva, Narva-Jõesuu",
#        3: "Kohtla-Järve",
#        4: "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa",
#        5: "Tartu linn",
#        6: "Tartumaa, Põlvamaa, Võrumaa, Valgamaa",
#        7: "Viljandimaa, Järvamaa, Harjumaa, Raplamaa",
#        8: "Pärnumaa",
#        9: "Läänemaa, Hiiumaa, Saaremaa"
#    }

#    if index in [1, 2, 3]:
#        print("Olevikus on olukord raske, palun püsi kodus!")
#    else:
#        print("Kandke maski!")
        
#    print("Postiindeks", index, "kuulub maakonda:", maakonnad.get(maakonna_number))

##5
#elementid = input("Sisestage elemendid: ").split(',')
#elementid = [int(element.strip()) for element in elementid]

#kogus = int(input("Sisestage elementide arv, mida soovite vahetada: "))

#while True:
#    if kogus < 2 or kogus > len(elementid)//2:
#        print("Vigane kogus! Palun sisestage vähemalt 2 ja mitte rohkem kui pool elementide arvust.")
#        break
#    else:
#        for i in range(kogus):
#            elementid[i], elementid[-(i + 1)] = elementid[-(i + 1)], elementid[i]
        
#        print("Uus list pärast vahetamist:", elementid)

##6
# Николай задумался о поиске «бесполезного» числа на основании списка.
#Суть оного в следующем: он берет произвольный список чисел, находит самое большое из них, а затем делит его на длину списка и заменяет его в списке результатом деления.

#import random
#list=[]
#for i in range(random.randint(10, 30)):
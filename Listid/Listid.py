##1

#glas = list("aeiouõäöüAEIOUÕÄÖÜаеёиоуыэюяАЕЁИОУЫЭЮЯ")
#sogl = list("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ")
#sumbolid = list(",.!?;:-—–()[]{}\"'")
#spaces=list(" ")
#while True:
#    sisend=str(input("Palun Sisestage sõna või lause /n>> "))
    
#    space = 0
#    g_arv = 0
#    s_arv = 0
#    sumb = 0
    
#    for char in sisend:
#        if char in glas:
#            g_arv += 1
#        elif char in sogl:
#            s_arv += 1
#        elif char in sumbolid:
#            sumb += 1
#        elif char in spaces:
#            space += 1
        
#    print(f"Vokaalid: {g_arv}")
#    print(f"Konsonandid: {s_arv}")
#    print(f"Sümbolid: {sumb}")
#    print(f"Tühikud: {space}")


## 2
#import random
#names = ['Juhan','Kati','Mario','Mario','Mati','Mati']
#print("Antud list: ", names)
#for i in range(len(names)):
#        if i == len(names):
#            break
#        n=names[i]
#        d=names.count(n)
#        if d>1:
#            for i in range(d-1):
#                names.remove(n)
#print("Parandatud list: ", names)
#print("Palun sisestage 5 nimed")
#for i in range(5):
#    while True:
#        name = input(f"Sisestage nimi ({i+1}): ")
#        names.append(name)
#        break
#        if name not in names:
#            names.append(name)
#            break
#        else:
#            print("See nimi on juba sisestatud. Palun sisestage teine nimi.")
#print(f"\nViimati sisestatud nimi: {names[-1]}")
#names.sort()
#ages = [random.randint(18, 30) for i in range(len(names))]
#for i, name in enumerate(names):
#   print(f"{name} - Vanus: {ages[i]} aastat")

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
#   change_name = input("\nKas soovite nimesid muuta? (y/n): ")
#   if change_name.lower() == 'n':
#       break
#   elif change_name.lower() == 'y':
#       change_name = input("\nSisestage nimi, mida soovite muuta: ")
#       if change_name in names:
#           index = names.index(change_name)
#           new_name = input("Sisestage uus nimi: ")
#           if new_name not in names:
#               names[index] = new_name
#           else:
#               print("See nimi on juba sisestatud. Palun sisestage teine nimi.")
#               continue
            
#           names.sort()
#           print("\nUuendatud nimede ja vanuste nimekiri:")
#           for i in range(len(names)):
#               print(f"{names[i]} - Vanus: {ages[i]} aastat")
            
#           print("\nVanuste statistika:")
#           print("Suurim vanus:", max_age)
#           print("Väikseim vanus:", min_age)
#           print("Vanuste summa:", total_age)
#           print("Keskmine vanus:", average_age)
#       else:
#           print("Sellist nime ei leitud. Palun sisestage olemasolev nimi.")
#   else:
#       continue

##3
#import random
#arvud=[]
#rida = int(input("Mitu?"))
#for p in range(rida):
#    arvud.append(random.randint(1,100))
#print(arvud)
#for p in range(rida):
#    print(arvud[p]*"*")


##4
#while true:
#   index=input("sisesta index: ")
#   if len(index) != 5 or not index.isdigit():
#       print("vigane postiindeks! palun sisestage 5 numbrist koosnev postiindeks.")
#       break
#   maakonna_number = int(index[0])
#   maakonnad = ["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa",
#                            "Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa",
#                            "Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#   print(maakonnad[maakonna_number-1])

#   if index in [1, 2, 3]:
#       print("Olevikus on olukord raske, palun püsi kodus!")
#   else:
#       print("Kandke maski!")


##5
#import random
#kogus = int(input("Sisestage soovitued elementide arv: "))
#elementid = [random.randint(1, 100) for i in range(kogus)]
#vahetada = int(input("Sisestage elementide arv, mida soovite vahetada: "))
#print("Genereeritud list: ", elementid)
#if vahetada < 2 or vahetada > len(elementid)//2:
#    print("Vigane kogus! Palun sisestage vähemalt 2 ja mitte rohkem kui pool elementide arvust.")
#else:
#    for i in range(vahetada):
#        elementid[i], elementid[-(i + 1)] = elementid[-(i + 1)], elementid[i]
#    print("Uus list pärast vahetamist:", elementid)

   
##6

#import random
#amount=random.randint(10, 40)
#numbers=[random.randint(1, 100) for i in range(amount)]
#print(numbers)
#while True:
#    numbers.sort()
#    print(numbers)
#    max=numbers[amount-1]
#    newmax=round(max/amount,1)
#    print("Maksimaalne arv:", max, "Loendis numbrite arv:", amount)
#    print("Jagamise tulemus:", round(max/amount,1))
#    numbers[numbers.index(max)]=newmax
#    numbers.sort()
#    print(numbers)

#    moveon = input("\nVeelkord?: (y/n): ")
#    if moveon.lower() == 'n':
#        break
#    elif moveon.lower() == 'y':
#        numbers.sort()
#        continue

# Iseseisev töö
#####################################################################################################
# #7
# numbers = []
# narv=int(input("Sisesta soovitud arvude arv: "))
# while True: 
#    for i in range(narv):    # Tsükli väärtuste lisamine
#        try: numbers.append(int(input(f"Sisesta arv {i}: ")))
#        except: print("Viga")
#    for i in range(narv):    # Tsükli sortimine absoluutväärtused mullimeetodi abil
#         for j in range(0, narv-i-1):
#             if abs(numbers[j]) < abs(numbers[j+1]):
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#    print("Numbrite nimekiri kasvavas järjestuses: ", numbers)
#    numbers.reverse()
#    print("Numbrite nimekiri kahanevas järjestuses: ", numbers)
#    break

# #8 
# import random
# sarv=int(input("Sisesta soovitud sõnade arv: "))
# sonad=[]
# while True: 
#     for i in range(sarv): # Sõnade loendisse lisamise tsükkel
#         try: sonad.append(str(input(f"Sisesta sõna {i}: ")))
#         except: print("Viga")
#     maxlen=0
#     for i in range(len(sonad)): # Tsükkel maksimaalse pikkusega sõna määramiseks
#         if maxlen<len(sonad[i]):
#             maxlen=len(sonad[i])
#     for i in range(len(sonad)): # Sõnade asenduse tsükkel
#         if int(len(sonad[i]))<maxlen:
#             sona=sonad[i]+"_"*(maxlen-len(sonad[i]))
#             sonad.insert(i+1, sona)
#             sonad.remove(sonad[i])
#     print ("Uus sama pikkusega stringide loend: \n",sonad)
#     break
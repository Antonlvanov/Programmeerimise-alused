#Iseseisev töö
####################################################################################################

# #7
# numbers = []
# narv=int(input("Sisesta soovitud arvude arv: "))
# while True: 
#    for i in range(narv):    # Tsükli väärtuste lisamine
#        try: numbers.append(int(input(f"Sisesta arv {i}: ")))
#        except: print("Viga")
#    for i in range(narv):    # Tsükli sortimine absoluutväärtused
#         for j in range(0, narv-i-1):
#             if abs(numbers[j]) < abs(numbers[j+1]):
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#    print("Numbrite nimekiri kasvavas järjestuses: ", numbers)
#    numbers.reverse()
#    print("Numbrite nimekiri kahanevas järjestuses: ", numbers)
#    break

# #8 
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

# #9
# glas = list("aeiouõäöüаеёиоуыэюя")
# sogl = list("bcdfghjklmnpqrstvwxzбвгджзйклмнпрстфхцчшщ")
# while True:
#     try: nimi=str(input("Mis sinu nimi on? \n"))
#     except: "Viga"
#     print(f"Tervist, {nimi.capitalize()}!")

#     g_arv = 0
#     s_arv = 0
#     nimil=[]

#     for char in nimi:
#        if char.lower() in glas:
#            g_arv += 1
#        elif char.lower() in sogl:
#            s_arv += 1
#        if nimil.count(char.lower())==0:
#            nimil.append(char.lower())
#     nimil.sort()
#     print(f"Vokaalide arv nimes: {g_arv}")
#     print(f"Konsonandide arv nimes: {s_arv}")
#     print(nimil)
#     break

# #11
# while True:
#     try: n=int(input("Sisestage tähtede arv järjestuses (1-26): "))
#     except: "Viga"
#     if 1 > n or n > 26:
#         print("Vale tähtede arv")
#         continue
#     letters = [chr(i+97) for i in range(n)]
#     print("Järjestus alaregistris olevatest tähtedest:", letters)

#     letters2 = [chr(i+97)*(i+1) for i in range(n)]
#     print("Järjestus korduvate tähtedega:", letters2)

# #12
# import random
# while True:
#     import random
#     arvud = [random.randint(1, 100) for i in range(10)] # Luuame loend
#     for arv in arvud: # Kutsutame loendist samu väärtusi
#         if arvud.count(arv)>1:
#             arvud.remove(arv)
#             arvud.append(random.randint(1, 100)) 
#     print("Luuatud loend:\n", arvud)

#     maxarv=arvud[arvud.index(max(arvud))] # Saame minimaalse ja maksimaalse väärtuse
#     minarv=arvud[arvud.index(min(arvud))]

#     indexmax=arvud.index(max(arvud)) # Saame max/min indeksid
#     indexmin=arvud.index(min(arvud))
#     print(maxarv," <<->> ",minarv)

#     arvud[indexmax] = minarv # min/max väärtusi vahetamine
#     arvud[indexmin] = maxarv

#     print("Uus loend:\n", arvud)
#     input("Veelkord?")
#     continue



# #1

# glas = list("aeiouõäöüAEIOUÕÄÖÜаеёиоуыэюяАЕЁИОУЫЭЮЯ")
# sogl = list("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ")
# sumbolid = list(",.!?;:-—–()[]{}\"'")
# spaces=list(" ")
# while True:
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


# # 2
# import random
# names = ['Juhan','Kati','Mario','Mario','Mati','Mati']
# print("Antud list: ", names)
# for i in range(len(names)):
#        if i == len(names):
#            break
#        n=names[i]
#        d=names.count(n)
#        if d>1:
#            for i in range(d-1):
#                names.remove(n)
# print("Parandatud list: ", names)
# print("Palun sisestage 5 nimed")
# for i in range(5):
#    while True:
#        name = input(f"Sisestage nimi ({i+1}): ")
#        names.append(name)
#        break
#        if name not in names:
#            names.append(name)
#            break
#        else:
#            print("See nimi on juba sisestatud. Palun sisestage teine nimi.")
# print(f"\nViimati sisestatud nimi: {names[-1]}")
# names.sort()
# ages = [random.randint(18, 30) for i in range(len(names))]
# for i, name in enumerate(names):
#   print(f"{name} - Vanus: {ages[i]} aastat")

# max_age = max(ages)
# min_age = min(ages)
# total_age = sum(ages)
# average_age = total_age/len(ages)

# print("\nVanuste statistika:")
# print("Suurim vanus:", max_age)
# print("Väikseim vanus:", min_age)
# print("Vanuste summa:", total_age)
# print("Keskmine vanus:", average_age)

# while True:
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

# #3
# import random
# arvud=[]
# rida = int(input("Mitu? \n"))
# for p in range(rida):
#    arvud.append(random.randint(1,100))
# print(arvud)
# for p in range(rida):
#    print(arvud[p]*"*")


# #4
# while true:
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


# #5
# import random
# kogus = int(input("Sisestage soovitued elementide arv: "))
# elementid = [random.randint(1, 100) for i in range(kogus)]
# vahetada = int(input("Sisestage elementide arv, mida soovite vahetada: "))
# print("Luuatud list: ", elementid)
# if vahetada < 2 or vahetada > len(elementid)//2:
#    print("Vigane kogus! Palun sisestage vähemalt 2 ja mitte rohkem kui pool elementide arvust.")
# else:
#    for i in range(vahetada):
#        elementid[i], elementid[-(i + 1)] = elementid[-(i + 1)], elementid[i]
#    print("Uus list pärast vahetamist:", elementid)

   
# #6

# import random
# amount=random.randint(10, 40)
# numbers=[random.randint(1, 100) for i in range(amount)]
# print(numbers)
# while True:
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

# #13

# import random 
# sõnad = ["Apple", "Banaan", "Pirn", "Ploom", "Arbuus", "Melon", "Kõrvits", "Kirss", "Kiivi", "Mandariin"]
# sõna = random.choice(sõnad)
# kuva = ["_"]*len(sõna)
# guessed = []
# attempts = 1
# max_attempts = 10
# print(" ".join(kuva))

# while True:
#     try:
#         guess = str(input("Sisesta tähestik: ").lower())
#     except: 
#         "Vale andme tüüp."
#     if len(guess)>1: "Palun sisesta ainult üks kiri!"
    
#     if guess in guessed:
#         print("Sa juba arvasid selle tähe ära!")
#         continue
    
#     if guess in sõna.lower():
#         print("Õige!")
#         guessed.append(guess)
#         kuva = ''
#         for letter in sõna.lower():
#             if letter in guessed:
#                 kuva += letter
#             else:
#                 kuva += '_'
#         print(kuva.capitalize())
#     else:
#         print("Vale!")
#         print("Püüdluste arv: ", attempts, "/10")
#         guessed.append(guess)
#         print(kuva)

#     if '_' not in kuva:
#         print("Sa arvasid sõna ära! Mõistatuslik sõna oli: ", sõna)
#         print(f"Kasutatud püüdluste arv: {attempts}/10")
#         break

#     attempts += 1
#     if attempts >=max_attempts:
#         print("Sa ei arvanud sõna ära!")
#         print(f"Kasutatud püüdluste arv: {attempts}/10")
#         break


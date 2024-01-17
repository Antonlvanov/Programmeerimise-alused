# #1
# st="Tere, maailm!"
# print(st)
# a = input("Palun siseda oma nimi")
# print(st + " Tervitan sind " + a)
# vanus = input("Palun siseda ome vanus")
# print(st + " Tervitan sind " + a + "! Sa oled " + vanus + " aastat vana.")

# #2
# vanus = 18 #int
# eesnimi = "jaak" #str
# pikkus = 16.5 #float
# kas_käib_koolis = true #bool
# #kood tüüpide kontrollimiseks
# print("Muutuja tüüp:", type(input("Vali muutuja. ")))

# #3
# kommid = 32
# print("Laual on " +str(kommid)+ " kommid.")
# print(kommid-int(input("Mitu kommi sa soovid laualt ära võtta? ")))

# #4
# def diameter(tree):
#     diameter = tree / 3.14
#     return diameter
# tree = float(input("Sisesta puu ümbermõõt (cm): "))
# tree_diameter = round(diameter(tree), 2)
# print("Diameeter on "+(str(tree_diameter))+" cm.")

# #5
# import math
# a = float(input("Sisesta ristkülikukujulise maatüki pikkus meetrites (M): "))
# b = float(input("Sisesta ristkülikukujulise maatüki laius (M): "))
# diag = round(math.sqrt(a**2 + b**2), 2)
# print(f"Ristkülikukujulise maatüki diagonaalipikkus on {diag} meetrit.")

# #6
# #Leidke järgnevast näiteprogrammist semantiline viga:
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = aeg / teepikkus #viga
# print("Sinu kiirus oli " + str(kiirus) + " km/h")

# #7
# sum = 0
# for i in range(5):
#     arv = int(input(f"Sisesta täisarv{i + 1}: "))
#     sum += arv
# kesk = sum / 5
# print("Arvude aritmeetiline keskmine on:", kesk)

# #8
# print("  @..@")
# print(" (----)")
# print("( \\__/ )")
# print("^^ \"\" ^^")

# #9
# a=1
# b=2
# c=3
# P=0
# for i in range(3):
#     arv = int(input(f"Sisesta kolmnurga küljed #{i + 1}: "))
#     P += arv
# print(P)

# #10
# pitsa = 12.9
# jootraha = 0.1
# P = int(input("Kui palju sõpru sul on?"))
# maks = round(float((pitsa+pitsa*0.1)/P), 2)
# print(maks)
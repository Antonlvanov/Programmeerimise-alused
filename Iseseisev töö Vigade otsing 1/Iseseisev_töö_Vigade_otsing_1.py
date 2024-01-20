from math import *
print("Ruudu karakteristikud")
try:
    a=float(input('Sisesta ruudu külje pikkus => '))
except ValueError:
    print("Viga! Palun sisestage kehtiv number.")
    exit(0)
S=a**2
print("Ruudu pindala", round(S,2))
P=4*a
print("Ruudu ümbermõõt", round(P,2)) # viga ""/''
di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
# print() #ei ole vaja
print('\n'"Ristküliku karakteristikud") #viga )
try:
    b=float(input("Sisesta ristküliku esimene külje pikkus => "))
except ValueError:
    print("Viga! Palun sisestage kehtiv number.")
    exit(0)
try:
    c=float(input("Sisesta ristküliku teine külje pikkus => "))
except ValueError:
    print("Viga! Palun sisestage kehtiv number.")
    exit(0)
S=b*c
print("Ristküliku pindala", round(S,2)) #viga '/" "
P=2*(b+c) #* on vajalik
print("Ristküliku ümbermõõt", round(P,2))
di=math.sqrt(b**2+c**2) # (b*2+c*2) >> (b**2+c**2)
print("Ristküliku diagonaal", round(di,2))
# print() #ei ole vaja
print('\n'"Ringi karakteristikud")
try:
    r=float(input("Sisesta ringi raadiusi pikkus =>"))
except ValueError:
    print("Viga! Palun sisestage kehtiv number.")
    exit(0)
d=2*r #* on vajalik
print("Ringi läbimõõt", round(d,2)) # ,
S=math.pi*(r**2) # S=pi()*r*2 >> S=math.pi*(r**2)
print("Ringi pindala", round(S,2)) # teist argumenti pole
C=2*math.pi*r #pi >> *math.pi
print("Ringjoone pikkus", round(C,2))
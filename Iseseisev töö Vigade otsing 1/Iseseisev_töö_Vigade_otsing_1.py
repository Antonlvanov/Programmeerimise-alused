import math # viga

def sisend(andmed, andmetüüp): # andmete tüüp kontrollimine
    while True:
        sisend_väärtus = input(andmed)
        try:
            return andmetüüp(sisend_väärtus)
        except ValueError:
            print("Viga! Palun sisestage õige tüüpi andmed.")

print("Ruudu karakteristikud")
a=sisend('Sisesta ruudu külje pikkus => ', float)
S=a**2
print("Ruudu pindala", round(S,2))
P=4*a
print("Ruudu ümbermõõt", round(P,2)) # viga ""/''
di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
# print() #ei ole vaja
print('\n'"Ristküliku karakteristikud") #viga )
b=sisend("Sisesta ristküliku 1. külje pikkus => ", float)
c=sisend("Sisesta ristküliku 2. külje pikkus => ", float)
S=b*c
print("Ristküliku pindala", round(S,2)) #viga '/" "
P=2*(b+c) #* on vajalik
print("Ristküliku ümbermõõt", round(P,2))
di=math.sqrt(b**2+c**2) # (b*2+c*2) >> (b**2+c**2)
print("Ristküliku diagonaal", round(di,2))
# print() #ei ole vaja
print('\n'"Ringi karakteristikud")
r=sisend("Sisesta ringi raadiusi pikkus =>", float)
d=2*r #* on vajalik
print("Ringi läbimõõt", round(d,2)) # ,
S=math.pi*(r**2) # S=pi()*r*2 >> S=math.pi*(r**2)
print("Ringi pindala", round(S,2)) # teist argumenti pole
C=2*math.pi*r #pi >> *math.pi
print("Ringjoone pikkus", round(C,2))
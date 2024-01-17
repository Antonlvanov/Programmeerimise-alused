import math # viga

def sisend(andmed, andmet��p): # andmete t��p kontrollimine
    while True:
        sisend_v��rtus = input(andmed)
        try:
            return andmet��p(sisend_v��rtus)
        except ValueError:
            print("Viga! Palun sisestage �ige t��pi andmed.")

print("Ruudu karakteristikud")
a=sisend('Sisesta ruudu k�lje pikkus => ', float)
S=a**2
print("Ruudu pindala", round(S,2))
P=4*a
print("Ruudu �mberm��t", round(P,2)) # viga ""/''
di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
# print() #ei ole vaja
print('\n'"Ristk�liku karakteristikud") #viga )
b=sisend("Sisesta ristk�liku 1. k�lje pikkus => ", float)
c=sisend("Sisesta ristk�liku 2. k�lje pikkus => ", float)
S=b*c
print("Ristk�liku pindala", round(S,2)) #viga '/" "
P=2*(b+c) #* on vajalik
print("Ristk�liku �mberm��t", round(P,2))
di=math.sqrt(b**2+c**2) # (b*2+c*2) >> (b**2+c**2)
print("Ristk�liku diagonaal", round(di,2))
# print() #ei ole vaja
print('\n'"Ringi karakteristikud")
r=sisend("Sisesta ringi raadiusi pikkus =>", float)
d=2*r #* on vajalik
print("Ringi l�bim��t", round(d,2)) # ,
S=math.pi*(r**2) # S=pi()*r*2 >> S=math.pi*(r**2)
print("Ringi pindala", round(S,2)) # teist argumenti pole
C=2*math.pi*r #pi >> *math.pi
print("Ringjoone pikkus", round(C,2))

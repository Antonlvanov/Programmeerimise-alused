import random
from secrets import choice
nimed=['mati', 'meelis', 'kati', 'mati']
while True:
    print("*************")
    v=input("N-näitada andmeid\nL-lisada andmeid\nK-andmete kutsutamine\nH-andmete haldus\n")
    if v=="N":
        v=input("Kas juhuslik(J) nimi või terve loetelu(T)?")
        if v=="T":
            print(nimed)
        elif v=="J":
            print(choice(nimed))
    elif v=="L":
        v=input("Kas nimekirja lõppu(L) või positsioonile(P)?")
        if v=="L":
            nimi=input("Sisesta nimi: ")
            nimed.append(nimi)
        elif v=="P":
            nimi=input("Sisesta nimi: ")
            ind=int(input("Mis kohale: "))
            nimed.insert(ind-1,nimi)
    elif v=="K":
        v=input("Kas nimi järgi(N) või indeksi järgi(I) või kõik nimed(K)?")
        if v=="I":
            v=int(input("Sisesta indeks: "))
            nimed.pop(ind-1)
        elif v=="N":
            nimi=input("Sisesta nimi: ")
            mitu=int(nimed.count(nimi))
            if mitu>0:
                for i in range(mitu):
                    nimed.remove(nimi)
            else:
                print(f"{nimi} ei ole loetelus")
        elif v=="K":
            nimed.clear()
    elif v=="H":
        v=input("Sorteerimine(S), Kopeerimine(K) või Ümber pööramine(P)")
        if v=="S":
            v=int(input("A-Z(1) või Z-A (2)"))
            if v==1:
                nimed.sort()
            if v==2:
                nimed.sort(reverse=True)
            print(nimed)
        elif v=="K":
            nimed.copy()
            print(nimed)
        elif v=="P":
            nimed.reverse()
            print(nimed)
    elif v=="I":
        v=input("Sisesta otsingut nimi: ")
        d=nimed.count(v)
        if d>1:
            for i in range(d):
                print(nimed.index(v, i))
        elif d==1:
            print(nimed.index(v))
        elif d==0:
            print("ei ole nimi")
                

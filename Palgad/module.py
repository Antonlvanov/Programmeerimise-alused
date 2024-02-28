from math import e

#1
def inimeste_ja_palkade_lisamine(i:list,p:list,n=1)->any:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka
    param list i: Inimeste järjend
    param list p: Palgate järjend
    param int n: Inimeste arv
    rtype: list, list
    """
    try:
        if n>0:
            for j in range(n):
                nimi=str(input(f"Nimi {j+1}: ")).capitalize() 
                palk=int(input(f"Palk {j+1}: ")) 
                i.append(nimi) 
                p.append(palk)
        return i,p
    except: "Vale sisend"
#0    
def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    param list i: Inimeste järjend
    param list p: Palgate järjend
    """
    for j in range(len(i)):
        print(i[j],"-",p[j]) 
#2
def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andmeid ja tagastab listid.
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    nimi=input("Keda kustutada ära(nimi): ") 
    for j in range(0,len(i)-1):
        if nimi in i:
            i.remove(nimi)
            p.pop(j)
    return i,p
#3
def kellel_on_suurim_palk(i:list,p:list)->any:
    """Funktsioon leiab kõige suurim palk
    param list i: Inimeste järjend
    param list p: Palgate järjend
    param int maxpalk: Sisestab suurem palk
    param list nimed: Sisestab suurem palk saatjad
    rtype: list, list
    """
    maxpalk=max(p) 
    nimed=[]
    for j in range(p.count(max(p))):
        nimed.append(i[p.index(max(p),p.index(max(p))+j)])
    return maxpalk,nimed
#4
def kellel_on_vaiksem_palk(i:list,p:list)->any:
    """Funktsioon leiab kõige väiksem palk 
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    param int maxpalk: Sisestab väiksem palk
    param list nimed: Sisestab väiksem palk saatjad
    """
    minpalk=min(p) 
    nimed=[]
    for j in range(p.count(min(p))):
        nimed.append(i[p.index(min(p),p.index(min(p))+j)])
    return minpalk,nimed
#5
def sorteeritud_palgad(i:list,p:list):
    """Funktsioon sorteerib palgad
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    try:
        s=int(input("Järjestada palgad kasvavas või kahanevas järjekorras? (1/2): "))
        if s==1:
            i.sort()
            p.sort()
            return i,p
        if s==2:
            i.sort()
            i.reverse()
            p.sort()
            p.reverse()
            return i,p
        else:
            print("Vale sisend")
    except: print("Vale sisend")
#6




    

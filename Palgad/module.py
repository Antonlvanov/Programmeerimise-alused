from math import e

#1
def inimeste_lisamine(i:list,p:list,n:int)->any:
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
    nimi=str(input("Keda kustutada ära? (nimi): ")).capitalize() 
    if nimi in i:
        p.pop(i.index(nimi))
        i.remove(nimi)
        print(nimi,"oli kutsutanud.")
    else: print("Ei leidnud")
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
    for k, x in enumerate(p):
        if x == maxpalk:
            nimed.append(i[k])
    return maxpalk,nimed
    # for j in range(p.count(max(p))):
    #     nimed.append(i[p.index(max(p),p.index(max(p))+j)])
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
    for k, x in enumerate(p):
        if x == minpalk:
            nimed.append(i[k])
    return minpalk,nimed
#5
def sorteeritud_palgad(i:list,p:list)->any:
    """Funktsioon sorteerib palgad
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    try:
        s=int(input("Järjestada palgad kahanevas (1) või kasvavas (2) järjekorras?: "))
    except: print("Vale sisend")
    for n in range(0,len(i)):
        for j in range(n,len(i)):
            if p[n]<p[j]:
                p[j],p[n]=p[n],p[j]
                i[j],i[n]=i[n],i[j]
        
    if s==1:
        print("Palgad kahanevas järjekorras:")
        for j in range(len(i)):
            print(i[j],"-",p[j])
    if s==2:
        print("Palgad kasvavas järjekorras:")
        i.reverse()
        p.reverse()
        for j in range(len(i)):
            print(i[j],"-",p[j])
    if 1>s or s>2:
        print("Vale sisend")
#6
def võrdset_palgad(i:list,p:list)->any:
    """Funktsioon leiab võrdset palgad 
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    param dict palgad: Sisestab kõik andmed
    """
    palgad={}
    for n in range(len(p)):
        if p.count(p[n])>1:
            palgad[p[n]] = [i[n]]
            for d in range(p.count(p[n])-1):
                palgad[p[n]].append(i[p.index(p[n],d)])
    return palgad

#7
def palgaotsing_nime_jargi(i:list,p:list)->any:
    """Palgaotsing nime järgi
    
    """
    try: nimi=str(input("Sisesta otsitav nimi: "))
    except:print("Vale sisend")
    leitud=[]
    for k in range(len(i)):
        if i[k] == nimi:
            leitud.append((i[k], p[k]))
    return leitud

#8 
def palga_vordlus(i:list,p:list)->any:
    try: summa=int(input("Sisesta summa: "))
    except: print("Vale sisend")
    suur=[]
    vaik=[]
    for k in range(len(p)):
        if p[k] > summa:
            suur.append((i[k], p[k])) 
        if p[k] < summa:
            vaik.append((i[k], p[k]))
    return suur,vaik,summa

#9 
def top_vaeseimad_rikkamad(i:list,p:list)->any:
    try: amount=int(input("Kui palju: "))
    except: print("Vale sisend")
    ks=[]
    for k in range(len(p)):
        klist=[i[k],p[k]]
        ks.append(klist)
    for n in range(len(p)):
        for k in range(n,len(p)):
            if ks[k][1]<ks[n][1]:
                ks[k],ks[n]=ks[n],ks[k]
    low=ks[:amount]
    high=ks[-amount:]
    high.reverse()
    return low,high

#10
def keskmine_palk(inimesed:list, palgad:list)->any:
    kesk=sum(palgad) / len(palgad)
    keskmine_inimene = []
    vaikseim_erinevus = float(1000)
    palk=[]
    for i in range(len(inimesed)):
        erinevus = abs(palgad[i] - kesk)
        if erinevus <= vaikseim_erinevus:
            vaikseim_erinevus = erinevus
            keskmine_inimene.append(inimesed[i])
            palk=palgad[i]
    return keskmine_inimene, palk

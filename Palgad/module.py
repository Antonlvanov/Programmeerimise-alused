from math import e

#1
def inimeste_ja_palkade_lisamine(i:list,p:list,n:int)->any:
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
        for n in range(0,len(i)):
            for m in range(n,len(i)):
                if p[n]<p[m]:
                    p[m],p[n]=p[n],p[m]
                    i[m],i[n]=i[n],i[m]
        s=int(input("Järjestada palgad kahanevas (1) või kasvavas (2) järjekorras?: "))
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
    except: print("Vale sisend")
#6
def võrdset_palgad(i:list,p:list)->any:
    """Funktsioon leiab kõige väiksem palk 
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    param int maxpalk: Sisestab väiksem palk
    param list nimed: Sisestab väiksem palk saatjad
    """
    korduvadpalgad={}
    for t in range(len(p)):
        if p[t] not in korduvadpalgad:
            korduvadpalgad[p[t]] = [i[t]]
        else:
            korduvadpalgad[p[t]].append(i[t])
    print(korduvadpalgad)
    uhis_list = [(p, i) for p, i in korduvadpalgad.items() if len(i) > 1]
    return uhis_list    



    

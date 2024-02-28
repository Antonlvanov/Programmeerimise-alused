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
def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    param list i: Inimeste järjend
    param list p: Palgate järjend
    """
    for j in range(len(i)):
        print(i[j],"-",p[j]) 
        
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

def kellel_on_suurim_palk(i:list,p:list)->any:
    """Funktsioon leiab kõige suurim palk
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    palk=max(p) 
    nimed=[]
    for j in range(p.count(max(p))):
        nimed.append(i[p.index(max(p),j)])
    return palk,nimed

def kellel_on_vaiksem_palk(i:list,p:list)->any:
    """Funktsioon leiab kõige väiksem palk 
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    palk=min(p) 
    n=p.count(palk) 
    positsiooni=0
    print("Minimaalne palk:"+str(palk)) 
    for j in range(n):
        ind=p.index(palk,positsiooni)
        nimi=i[ind] 
        print(f"{nimi} on minimaalne palk") 
        positsioni=ind+1 
        return i,p 


def sorteeritud_palgad(i:list,p:list):
    """Funktsioon sorteerib palgad
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[m],p[n]=p[n],p[m]
                i[m],i[n]=i[n],i[m]
    return i,p 




    

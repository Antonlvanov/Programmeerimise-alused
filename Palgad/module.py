

#0    
def andmed_veerudes(i:list,p:list):
    """Funktsioon kuvab ekraanile kahe järjendite andmed veerudes
    param list i: Inimeste järjend
    param list p: Palgate järjend
    """
    for j in range(len(i)):
        print(f"#{j+1} {i[j]} - {p[j]}") 

#1
def inimeste_lisamine(i:list,p:list)->any:
    """Funktsioon tagastab uuendatud loendid, kus lisatud inimesi ja palka
    param list i: Inimeste järjend
    param list p: Palgate järjend
    param int n: Inimeste arv
    rtype: list, list
    """
    n = int(input("Mitu inimest lisame? "))
    if n>0:
        for j in range(n):
            nimi=str(input(f"Nimi {j+1}: ")).capitalize() 
            palk=int(input(f"Palk {j+1}: ")) 
        i.append(nimi) 
        p.append(palk)
        return i,p

#2
def andmete_eemaldamine_nimi_jargi(i:list,p:list)->any:
    """Funktsioon kustutab andmeid ja tagastab listid.
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    try:nimi=str(input("Keda kustutada ära? (nimi): ")).capitalize() 
    except: "Vale sisend"
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
    print("Suurem palk on",maxpalk,"\nSaatja(d):", ", ".join(nimed))
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
    print("Väiksem palk on",minpalk,"\nSaatja(d):", ", ".join(nimed))

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
    for key,i in palgad.items():
        plgv= ", ".join(i)
        print(f"Palk: {key} Palga saatjad: {plgv}")

#7
def palgaotsing_nime_jargi(i:list,p:list)->any:
    """Palgaotsing nime järgi
    
    """
    try: nimi=str(input("Sisesta otsitav nimi: "))
    except:print("Vale sisend")
    if nimi in i:
        leitud=[]
        for k in range(len(i)):
            if i[k] == nimi:
                leitud.append(i[k])
                leitud.append(p[k])
        for i in range(0,len(leitud),2):
            print(f"{leitud[i]}: {leitud[i+1]}")
    else: print("Nimi ei leitud")

#8 
def palga_vordlus(i:list,p:list)->any:
    try: summa=int(input("Sisesta summa: "))
    except: print("Vale sisend")
    suur=[]
    vaik=[]
    for k in range(len(p)):
        if p[k] > summa:
            suur.append(i[k])
            suur.append(p[k])
        if p[k] < summa:
            vaik.append(i[k])
            vaik.append(p[k])
    print("Saavad rohkem:")
    for i in range(0,len(suur),2):
        print(f"{suur[i]}: {suur[i+1]}")
    print("Saavad vähem:")
    for i in range(0,len(vaik),2):
        print(f"{vaik[i]}: {vaik[i+1]}")

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
    print("Vaeseimad inimesed:")
    for i in range(len(low)):
        print(f"{low[i][0]}: {low[i][1]}")
    print("Rikkamad inimesed:")
    for i in range(len(high)):
        print(f"{high[i][0]}: {high[i][1]}")

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
    print(f"Keskmine palk: {palk}")
    print(f"Saatja(d): {', '.join(map(str, keskmine_inimene))}")

#11
def tulumaks(inimesed:list, palgad:list, eilahe=654, tulumaks=0.20)->any:
    pal=palgad.copy()
    for i in range(len(palgad)):
        netopalk = pal[i]-((pal[i] - eilahe)*tulumaks)
        pal[i] = int(netopalk)
    for j in range(len(pal)):
        print(f"#{j+1} {inimesed[j]} - {pal[j]}") 

#12
def sort_by_name(inimesed:list, palgad:list)->any:
    spisok=[]
    for i in range(len(inimesed)):
        spisok.append((inimesed[i], palgad[i]))
        spisok.sort()
    for i in range(len(inimesed)):
        inimesed[i]=spisok[i][0]
        palgad[i]=spisok[i][1]
    andmed_veerudes(inimesed,palgad)
    
#13
def remove_below_average(inimesed:list, palgad:list)->any:
    keskpalk = keskmine_palk(inimesed,palgad)[1]
    indlist=[]
    for i in range(len(inimesed)):
        if palgad[i] < keskpalk:
            indlist.append(i)
    indlist.reverse()
    for i in range(len(indlist)):
        del palgad[indlist[i]]
        del inimesed[indlist[i]]
    andmed_veerudes(inimesed,palgad)

#14
import re
def muuda_listid(inimesed:list, palgad:list)->any:
    for i in range(len(inimesed)):
        inimesed[i]=str(inimesed[i]).capitalize()
        int(palgad[i])
    print("Palgad tüüp:",re.findall(r"'(.*?)'", str(type(palgad[1])))[0])
    andmed_veerudes(inimesed,palgad)

#15
def tosta_palka(inimesed:list, palgad:list)->any:
    pal=[]
    pal=palgad.copy()
    aastat=int(input("Mitu aastat loenda? "))
    for d in range(aastat):
        for i in range(len(palgad)):
            pal[i] *= 1.05
            pal[i] = int(pal[i])
    print("Uuendatud list:")
    for j in range(len(pal)):
        print(f"#{j+1} {inimesed[j]} - {pal[j]}") 
    

#16
def nimetada_iga_kolme(inimesed:list, palgad:list)->any:
    """Funktsioon umber nimetab iga kolme inimeste ja tagastab listid.
    param list i: Inimeste järjend
    param list p: Palgate järjend
    rtype: list, list
    """
    for i in range(2, len(inimesed), 3):
        if i<len(inimesed):
            try:nimi=str(input(f"Sisesta uus nimi? #{i}: ")).capitalize()
            except: print("Vale sisend")
            inimesed[i] = nimi
        else: continue
    print("Uuendatud list:")
    andmed_veerudes(inimesed,palgad)

#17
def muuta_andmeid(inimesed:list, palgad:list)->any:
    nimi=str(input("Kelle andmed soovite muutuda?: ")).capitalize()
    if nimi in inimesed:
        valik=input("Mida soovite redigeerida? (Nimi - 1 / Palk - 2): ")
        if valik == "1":
            uusnimi=str(input("Uus nimi: ")).capitalize()
            if inimesed.count(uusnimi)==0:
                inimesed[inimesed.index(nimi)]=uusnimi
                print("Uuendatud list:")
                andmed_veerudes(inimesed,palgad)
                return 0
            else:
                print("See nimi on juba hõivatud.")
        if valik == "2":
            palgad[inimesed.index(nimi)]=int(input("Sisesta uus palk: "))
            print("Uuendatud list:")
            andmed_veerudes(inimesed,palgad)
        else: 
            print("Vale valik")
    else: print("Nimi ei leidnud")

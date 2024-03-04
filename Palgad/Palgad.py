from module import *
palgad=[1200,2500,750,395,1200,395,600]
inimesed=["A","G","C","D","E","F","F"]
while True:
    print("\n0-Naita andmed veerudes\n1-andemete lisamine\n2-andmete kustutamine\n3-kõige suurim palk\n4-kõige väiksem palk\n5-sorteeritud palgad\n6-võrdset palgad\n7-palgaotsing nime järgi\n") 
    try: valik=int(input())
    except: 
        print("Vale sisend")
        continue
    if 0<=valik<20:
        if valik==1:
            inimesed,palgad=inimeste_ja_palkade_lisamine(inimesed,palgad,int(input("Mitu inimest lisame? ")))
            andmed_veerudes(inimesed,palgad)
        elif valik==0:
            andmed_veerudes(inimesed,palgad)
        elif valik==2:
            andmete_eemaldamine_nimi_jargi(inimesed, palgad) 
        elif valik==3:
            palk,nimed=kellel_on_suurim_palk(inimesed, palgad)
            print("Suurem palk on",palk,"\nSaatja(d):", ", ".join(nimed))
        elif valik==4:
            palk,nimed=kellel_on_vaiksem_palk(inimesed, palgad)
            print("Väiksem palk on",palk,"\nSaatja(d):", ", ".join(nimed))
        elif valik==5:
            sorteeritud_palgad(inimesed, palgad)
        elif valik==6:
            plg=võrdset_palgad(inimesed, palgad)
            for key, i in plg.items():
                plgv= ", ".join(i)
                print(f"Palk: {key} Palga saatjad: {plgv}")
        elif valik==7:
            print(palgaotsing_nime_jargi(inimesed,palgad))
        elif valik==8:
            vaik,suur,summa=palga_vordlus(inimesed,palgad)
            print(f"Väiksem: {vaik}")
            print(f"Suurem: {suur}")
    else: 
        print("Vale number")
        continue   

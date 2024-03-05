from module import *
palgad=[1200,2500,750,395,1200,395,600]
inimesed=["a","G","C","D","E","F","F"]
while True:
    print("""
          \n0-Naita andmed veerudes\n1-andemete lisamine\n2-Andmete kustutamine\n3-Kõige suurim palk\n4-Kõige väiksempalk\n5-Sorteeritud palgad\n6-Võrdset palgad\n7-Palgaotsing nime järgi\n8-Kes saavad rohkem/vähem kui määratudsumma\n9-Vaeseimad ja rikkamad inimesed\n10-Keskmine palk ja selle saaja nimed\n11-Palgad pärast tulumaksu arvestamist\n12-Sorteeri nime järgi\n13-Eemaldada need, kes saavad keskmisest madalamat palka\n14-Nimed suurtähtedega, palgad int formaadis.\n
          """)
    try: valik=int(input())
    except: 
        print("Vale sisend")
        continue
    if 0<=valik<20:
        if valik==0:
            andmed_veerudes(inimesed,palgad)
        elif valik==1:
            inimesed,palgad=inimeste_lisamine(inimesed,palgad,int(input("Mitu inimest lisame? ")))
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
            for key,i in plg.items():
                plgv= ", ".join(i)
                print(f"Palk: {key} Palga saatjad: {plgv}")
        elif valik==7:
            print(palgaotsing_nime_jargi(inimesed,palgad))
        elif valik==8:
            vaik,suur,summa=palga_vordlus(inimesed,palgad)
            print(f"Väiksem: {vaik}")
            print(f"Suurem: {suur}")
        elif valik==9:
            low,high=top_vaeseimad_rikkamad(inimesed, palgad)
            print("Vaeseimad inimesed:")
            for i in range(len(low)):
                print(f"{low[i][0]}: {low[i][1]}")
            print("Rikkamad inimesed:")
            for i in range(len(high)):
                print(f"{high[i][0]}: {high[i][1]}")
        elif valik==10:
            keskinim,palk=keskmine_palk(inimesed,palgad)
            print(f"Keskmine palk: {palk}")
            print(f"Saatja(d): {', '.join(map(str, keskinim))}")
        elif valik==11:
            tulumaks(inimesed,palgad)
        elif valik==12:
            sort_by_name(inimesed,palgad)
        elif valik==13:
            remove_below_average(inimesed,palgad)
        elif valik==14:
            edit_lists(inimesed,palgad)
    else: 
        print("Vale number")
        continue   

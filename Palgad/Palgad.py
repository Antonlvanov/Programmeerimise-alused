from module import *
palgad=[1200,2500,750,395,1200,395,600]
inimesed=["A","G","C","D","E","F","F"]
while True:
    print("""
          \n0-Naita andmed veerudes\n1-andemete lisamine\n2-Andmete kustutamine\n3-Kõige suurim palk\n4-Kõige väiksempalk\n5-Sorteeritud palgad\n6-Võrdset palgad\n7-Palgaotsing nime järgi\n8-Kes saavad rohkem/vähem kui määratudsumma\n9-Vaeseimad ja rikkamad inimesed\n10-Keskmine palk ja selle saaja nimed\n11-Palgad pärast tulumaksu arvestamist\n12-Sorteeri nime järgi\n13-Eemaldada need, kes saavad keskmisest madalamat palka\n14-Nimed suurtähtedega, palgad int formaadis.\n
          """)
    try:
        v=int(input())
    except: 
        print("Vale andmed")
    if 0<=v<20:
        if v==0:
            andmed_veerudes(inimesed,palgad)
        elif v==1:
            inimesed,palgad=inimeste_lisamine(inimesed,palgad)
            andmed_veerudes(inimesed,palgad)
        elif v==2:
            andmete_eemaldamine_nimi_jargi(inimesed, palgad) 
        elif v==3:
            kellel_on_suurim_palk(inimesed, palgad)
        elif v==4:
            kellel_on_vaiksem_palk(inimesed, palgad)
        elif v==5:
            sorteeritud_palgad(inimesed, palgad)
        elif v==6:
            võrdset_palgad(inimesed, palgad)
        elif v==7:
            palgaotsing_nime_jargi(inimesed,palgad)
        elif v==8:
            palga_vordlus(inimesed,palgad)
        elif v==9:
            top_vaeseimad_rikkamad(inimesed, palgad)
        elif v==10:
            keskmine_palk(inimesed,palgad)
        elif v==11:
            tulumaks(inimesed,palgad)
        elif v==12:
            sort_by_name(inimesed,palgad)
        elif v==13:
            remove_below_average(inimesed,palgad)
        elif v==14:
            muuda_listid(inimesed,palgad)
        elif v==15:
            tosta_palka(inimesed,palgad)
        elif v==16:
            nimetada_iga_kolme(inimesed,palgad)
        elif v==17:
            muuta_andmeid(inimesed,palgad)
    else: 
        print("Vale number")
        continue
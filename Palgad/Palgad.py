﻿from module import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"] 
while True:
    print("\n0-Naita andmed veerudes\n1-andemete lisamine\n2-andmete kustutamine\n3-kõige suurim palk\n4-kõige väiksem palk\n5-sorteeritud palgad\n") 
    try:
        valik=int(input())
        if 0<valik<20:
            if valik==1:
                inimesed,palgad=inimeste_ja_palkade_lisamine(inimesed,palgad,int(input("Mitu inimest lisame? ")))
                andmed_veerudes(inimesed,palgad)
            elif valik==0:
                andmed_veerudes(inimesed,palgad)
            elif valik==2:
                andmete_eemaldamine_nimi_jargi(inimesed, palgad) 
            elif valik==3:
                palk,nimed=kellel_on_suurim_palk(inimesed, palgad)
                print("Maksimaalne palk on",palk,"\nSaatja(d):", ", ".join(nimed))
            elif valik==4:
                kellel_on_vaiksem_palk(inimesed, palgad)
            elif valik==5:
                sorteeritud_palgad(inimesed, palgad) 
                print(inimesed, palgad) 
                print(inimesed, palgad)
        else: 
            print("Vale sisend")
            continue   
    except: print("Viga")
from module1 import *

kasutajad=["A","G","C","D","E"]
paroolid=[]
for i in range(len(kasutajad)):
    k=''
    paroolid.append(salasona_genereerimine(k))
while True:
    print("\n1 Registreetimine\n2 Autoriseerimine\n3 Parooli taastamine\n4 Kinnita")
    print()
    try:
        v=int(input())
    except: 
        print("Vale andmed")
    if 0<=v<7:
        if v==1:
            registreerimine(kasutajad,paroolid)
        elif v==3:
            unustanud_parooli_taastamine(kasutajad,paroolid)
        elif v==4:
            exit(0)
        elif v==2:
            while autoriseerimine(kasutajad,paroolid):
                print("\n1 Unustanud parooli taastamine\n2 Nimi või parooli muutumine")
                c=int(input())
                if c==1:
                    unustanud_parooli_taastamine(kasutajad,paroolid)
                    continue
                if c==2:
                    nime_voi_parooli_muutmine(kasutajad,paroolid)
                    continue
    else: 
        print("Vale number")
        continue
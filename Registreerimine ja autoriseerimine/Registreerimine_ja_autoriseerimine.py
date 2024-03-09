from module1 import *
from Failid import *

kasutajad=["Anna","Grisha","Sasha","Daniil","Eren"]
paroolid=[]
emailid=[]
template()
for i in range(len(kasutajad)):
    k=''
    paroolid.append(salasona_genereerimine(k))
    emailid.append(str(kasutajad[i])+"@tthk.ee")

while True:
    print("\n1 Registreetimine \n2 Autoriseerimine \n3 Parooli taastamine\n4 Kinnita")
    print()
    v=0
    try:
        v=int(input())
    except: 
        print("Vale andmed")
    if 0<=v<7:
        if v==1:
            registreerimine(kasutajad,paroolid,emailid)
        elif v==3:
            unustanud_parooli_taastamine(kasutajad,paroolid,emailid)
        elif v==4:
            exit(0)
        elif v==2:
            re,kasutajanimi=autoriseerimine(kasutajad,paroolid)
            if re==True:
                print("\n1 Unustanud parooli taastamine\n2 Näita kõik kasutajad andmeid")
                c=int(input())
                if c==1:
                    oma_nimi_voi_parooli_muutmine(kasutajad,paroolid,kasutajanimi)
                    continue
                if c==2:
                    näita_koik_kasutajad_andmeid(kasutajad,paroolid)
                    continue
            else: continue
    else: 
        print("Vale number")
        continue

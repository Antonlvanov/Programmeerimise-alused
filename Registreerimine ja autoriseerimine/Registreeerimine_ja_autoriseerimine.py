from Funktsioonid import *

write_data_from_list()
while True:
    v=0
    try:
        v=int(input("\n1 Registreetimine \n2 Autoriseerimine \n3 Parooli taastamine\n4 Kinnita\n"))
    except: 
        print("Vale sisend")
    if 0<v<7:
        if v==1:
            registreerimine()
        elif v==3:
            unustanud_parooli_taastamine()
        elif v==4:
            exit(0)
        elif v==2:
            kasutaja=autoriseerimine()
            if kasutaja!=False:
                print("\n1 Muutuda oma andmed\n2 Näita kõik kasutajad andmeid")
                c=int(input())
                if c==1:
                    oma_andme_muutmine(kasutaja)
                    continue
                if c==2:
                    näita_koik_kasutajate_andmed()
                    continue
            else: continue
    else: 
        print("Vale number")
        continue


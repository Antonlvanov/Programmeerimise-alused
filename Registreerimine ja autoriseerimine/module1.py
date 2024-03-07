import string
import random

def salasona_genereerimine(k:str):
    for i in range(12):
        t=random.choice(string.ascii_letters) 
        num=random.choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        k+=random.choice(t_num)
    k+=random.choice("""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/""")
    return k

def registreerimine(kasutajad:list, paroolid:list)->any:
    try: nimi=str(input("Sisesta soovitud nimi: ")).capitalize()
    except: "Vale sisend"
    kasutajad.append(nimi)
    val=int(input("Valige kas te soovite automaatne parooli genereerimine (1) või luua parooli ise (2): "))
    parool=str()
    if val==1:
        parool=salasona_genereerimine(parool)
        paroolid.append(parool)
        print(f"{nimi}! Genereeritud salasõna on {parool}")
        print("Konto edukalt registreeritud!")
        return
    if val==2:
        paroolid.append(input("Sisesta soovitud salasõna: "))
        print("Konto edukalt registreeritud!")
        return
    else:
        print("Vale valik")

def autoriseerimine(kasutajad:list, paroolid:list)->any:
    try: kasutajanimi=(str(input("Kasutaja nimi: "))).capitalize()
    except: print("Vale sisend")
    if kasutajanimi in kasutajad:
        try: parool=(str(input("Salasõna: ")))
        except: print("Vale sisend")
        if paroolid[kasutajad.index(kasutajanimi)]==parool:
            print("Sisselogimine on edukalt!")
            return True
        else: print("Vale salasõna")
        return False
    else: print("Kasutaja ei leidnud")
    return False
    
def unustanud_parooli_taastamine(kasutajad:list, paroolid:list)->any:
    try: kasutajanimi=(str(input("Kasutaja nimi: "))).capitalize()
    except: print("Vale sisend")
    if kasutajanimi in kasutajad:
        print("Teie parool on: ",paroolid[kasutajad.index(kasutajanimi)])
    else: print("Kasutaja ei leidnud.")

def nime_voi_parooli_muutmine(kasutajad:list, paroolid:list)->any:
    s=int(input("Kas tahate muutuda nimi(1) või salasõna(2)? "))
    if s==1:
        try: kasutajanimi=(str(input("Uus nimi: "))).capitalize()
        except: print("Vale sisend")
        kasutajad[kasutajad.index(kasutajanimi)]==kasutajanimi
        print("Kasutaja nimi oli muudatud")
    if s==2:
        try: kasutajanimi=(str(input("Sisesta oma kasutajanimi: "))).capitalize()
        except: print("Vale sisend")
        try: uusparool=(str(input("Sisesta uus salasõna: ")))
        except: print("Vale sisend")
        spec="""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/"""
        if uusparool.isdigit() and uusparool.isupper() and uusparool.islower() and any(c in spec for c in s):
            paroolid[kasutajad.index(kasutajanimi)]
            print("Salasõna oli muudatud")
        else: print("Parool peab siselda numbrid, tähed põhjastähti, suurtähti ja spetsialist tähed.")
    else:
        print("Vale valik")


#def näita_koik_kasutajad:

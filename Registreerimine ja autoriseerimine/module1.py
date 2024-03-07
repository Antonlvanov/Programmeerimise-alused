import string
import random

def salasona_genereerimine(k:str):
    for i in range(12):
        t=random.choice(string.ascii_letters) 
        num=random.choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        k+=random.choice(t_num)
    k+=random.choice("!@#$%^&*")
    return k

def check_password(password:str)->any:
    special = str("!@#$%^&*")
    upper = False
    lower = False
    digit = False
    in_special=False
    pw_len=True
    if len(password)<8 or len(password)>16:
        pw_len=False
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            digit = True
        elif char in special:
            in_special = True
    if (upper and lower and digit and special and pw_len):
        return True 
    else:
        print("\nSalasõna peab sisaldama:\n8-16 tähte \nAlumise registri tähti \nÜlemise registri tähti \nNumbreid \nErimärke (!@#$%^&*)")
        return False

def check_name(kasutajad:list,name:str)->any:
    if name in kasutajad:
        print("Nimi on juba hõivatud")
        return False
    if (len(name))>=4 and (len(name))<=16:
        return True
    else:
        print("Nimi peab sisaldama 4-16 tähte")
        return False

def registreerimine(kasutajad:list, paroolid:list)->any:
    nimi=str(input("Sisesta soovitud nimi: "))
    if check_name(kasutajad,nimi):
        kasutajad.append(nimi)
        val=int(input("Valige kas te soovite automaatne parooli genereerimine (1) või luua parooli ise (2): "))
        parool=""
        if val==1:
            parool=salasona_genereerimine(parool)
            paroolid.append(parool)
            print(f"{nimi}! Genereeritud salasõna on {parool}")
            print("Konto edukalt registreeritud!")
            pass
        while True:
            if val==2:
                pw=str(input("\nSisesta soovitud salasõna: "))
                if check_password(pw):
                    paroolid.append(pw)
                    print("Konto edukalt registreeritud!")
                    break
                else:
                    pass
    else: pass

def autoriseerimine(kasutajad:list, paroolid:list)->any:
    try: kasutajanimi=(str(input("Kasutaja nimi: ")))
    except: print("Vale sisend")
    if kasutajanimi in kasutajad:
        try: parool=str(input("Salasõna: "))
        except: print("Vale sisend")
        if paroolid[kasutajad.index(kasutajanimi)]==parool:
            print("Sisselogimine on edukalt!")
            return True, kasutajanimi
        else: print("Vale salasõna")
        return False, kasutajanimi
    else: print("Kasutaja ei leidnud")
    return False, kasutajanimi
    
def unustanud_parooli_taastamine(kasutajad:list, paroolid:list)->any:
    try: kasutajanimi=(str(input("Kasutaja nimi: ")))
    except: print("Vale sisend")
    if kasutajanimi in kasutajad:
        print("Teie parool on: ",paroolid[kasutajad.index(kasutajanimi)])
    else: print("Kasutaja ei leidnud.")

def ome_nimi_voi_parooli_muutmine(kasutajad:list, paroolid:list, kasutajanimi:str)->any:
    while True:
        try:
            s=int(input("Kas tahate muutuda nimi(1) või salasõna(2)? (väljuda - 3) "))
            if s==1:
                try: uusnimi=(str(input("Uus nimi: ")))
                except: print("Vale sisend")
                if check_name(kasutajad,uusnimi):
                    kasutajad[kasutajad.index(kasutajanimi)]=uusnimi
                    print("Kasutaja nimi oli muudatud")
                    break
                else:
                    pass
            if s==2:
                password=input("Sisesta uus salasõna: ")
                if check_password(password):
                    paroolid[kasutajad.index(kasutajanimi)]=password
                    print("Salasõna oli muudatud")
                    break
                else:
                    pass
            if s==3:
                break
            else:
                continue
        except:print("Viga")
        
def näita_koik_kasutajad_andmeid(kasutajad:list, paroolid:list)->any:
    for j in range(len(kasutajad)):
        print(f"#{j+1} {kasutajad[j]} - {paroolid[j]}")

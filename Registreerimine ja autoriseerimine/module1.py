from Failid import *
import string
import random
import smtplib,ssl
from email.message import EmailMessage

def send_mail(kasutaja:str, password:str, email:str)->any:
    smtp_server="smtp.gmail.com"
    port = 587
    emailkeywords="moch cerq cnsz rrhd"
    context=ssl.create_default_context()
    #msg
    msg = EmailMessage()
    msg.set_content(f"Tere {kasutaja}! Teie parool on: {password}")
    msg['Subject']="Parooli taastamine"
    msg['From']=sender_mail="anton9032@gmail.com"
    msg['To']=email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() #can be omitted
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_mail, emailkeywords)
        server.send_message(msg)
    except Exception as e:
        print(e)
    finally:
        return True
        print("Email oli saadetud")
        server.quit()
    
def salasona_genereerimine(pw:str):
    for i in range(12):
        t=random.choice(string.ascii_letters) 
        num=random.choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        pw+=random.choice(t_num)
    pw+=random.choice("!@#$%^&*")
    return pw

def check_password(password:str)->any:
    special = str("!@#$%^&*")
    upper=lower=digit=in_special=False
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
    if (upper and lower and digit and in_special and pw_len):
        return True 
    else:
        print("\nParool peab sisaldama:\n8-16 tähte \nAlumise registri tähti \nÜlemise registri tähti \nNumbreid \nErimärke (!@#$%^&*)")
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

def check_mail(email:str)->any:
    if '@' in email and "." in email:
        return True
    else:
        print("Vale posti adress")
        return False

def registreerimine(kasutajad:list, paroolid:list, emailid:list)->any:
    while True:
        nimi=str(input("Sisesta soovitud nimi: "))
        if check_name(kasutajad,nimi):
            kasutajad.append(nimi)
        else: continue
        while True:
            mail=str(input("Sisesta postiadress: "))
            if check_mail(mail):
                emailid.append(mail)
                break
            else:
                continue
        while True:
            v=input("\nValige üks:\n\nAutomaatne parooli genereerimine - 1\nLuua parooli ise - 2\n")
            if v=="1":
                parool=salasona_genereerimine('')
                paroolid.append(parool)
                print(f"Genereeritud parool on: {parool}")
                print("Konto edukalt registreeritud!")
                break
            if v=="2":
                while True:
                    pw=str(input("\nSisesta soovitud parooli: "))
                    if check_password(pw):
                        paroolid.append(pw)
                        print("Konto edukalt registreeritud!")
                        break
                    else:
                        continue
                    break
                break
            else:
                print("Vale valik")
                continue
        break

def autoriseerimine(kasutajad:list, paroolid:list)->any:
    try: kasutajanimi=str(input("Kasutaja nimi: "))
    except: print("Vale sisend")
    if kasutajanimi in kasutajad:
        try: parool=str(input("Parooli: "))
        except: print("Vale sisend")
        if paroolid[kasutajad.index(kasutajanimi)]==parool:
            print("Sisselogimine on edukalt!")
            return True, kasutajanimi
        else: print("Vale parool")
        return False, kasutajanimi
    else: print("Kasutaja ei leidnud")
    return False, kasutajanimi
    
def unustanud_parooli_taastamine(kasutajad:list, paroolid:list, emailid:list)->any:
    while True:
        sisend=str(input("Sisesta teie kasutaja nimi või e-posti adress: "))
        if sisend in kasutajad:
            if send_mail(sisend,paroolid[kasutajad.index(sisend)],emailid[kasutajad.index(sisend)]):
                print("Teie parool oli saadetud e-postile: ",emailid[kasutajad.index(sisend)])
                break
        if sisend in emailid:
            if send_mail(kasutajad[emailid.index(sisend)],paroolid[emailid.index(sisend)],sisend):
                print(kasutajad[emailid.index(sisend)],"! Teie parool oli saadetud e-postile.")
            break
        else: print("Kasutaja ei leidnud.")
        

def oma_nimi_voi_parooli_muutmine(kasutajad:list, paroolid:list, kasutajanimi:str)->any:
    while True:
        try:
            s=int(input("Kas tahate muutuda nimi(1) või parool(2)? (väljuda - 3) "))
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
                password=input("Sisesta uus parool: ")
                if check_password(password):
                    paroolid[kasutajad.index(kasutajanimi)]=password
                    print("Parool oli muudatud")
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
        

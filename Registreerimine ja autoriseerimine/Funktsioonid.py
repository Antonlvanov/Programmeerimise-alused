from Failid import *
import string
import random
import smtplib,ssl
from email.message import EmailMessage
    
def salasona_genereerimine():
    pw=''
    for i in range(12):
        t=random.choice(string.ascii_letters) 
        num=random.choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        pw+=random.choice(t_num)
    pw+=random.choice("!@#$%^&*")
    return pw

def check_name(name)->any:
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
        print()
        return False

def registreerimine()->any:
    while True:
        username=input("Sisesta soovitud nimi: ")
        if len(username)<4 or len(username)>16:
            print("Nimi peab sisaldama 4-16 tähte")
            continue
        find = find_user_data(username)
        if find is not None and not find.empty:
            print("Nimi on juba hõivatud")
            if input("Proovi uuesti? (y/n):")=="y": continue
            else: return False
        else: break
    while True:
        email=input("Sisesta soovitud email: ")
        if check_mail(email):
            find = find_user_data(email)
            if find is not None and not find.empty:
                print("Selle email on juba registreeritud!")
                continue
            else: pass
            break
        else: continue
    while True:
        v=input("\nValige üks:\n\nAutomaatne parooli genereerimine - 1\nLuua parooli ise - 2\n")
        if v=="1":
            password=salasona_genereerimine()
            print(f"Genereeritud parool on: {password}")
            user_to_file_by_template(username,email,password)
            print("Konto edukalt registreeritud!")
            return True
        if v=="2":
            while True:
                pw=str(input("\nSisesta soovitud parooli: "))
                if check_password(pw):
                    user_to_file_by_template(username,email,password)
                    print("Konto edukalt registreeritud!")
                    return True
                if input("Proovi uuesti? (y/n):")=="y":
                    continue
                else:
                    return False
        else:
            print("Vale valik")
            continue

def autoriseerimine()->any:
    while True:
        kasutajanimi=input("Kasutaja nimi: ")
        find = find_user_data(kasutajanimi)
        if find is not None and not find.empty:
            if find['Kasutaja']==kasutajanimi :
                while True:
                    parool=str(input("Parool: "))
                    if find['Parool'] == parool:
                        print("Sisselogimine on edukalt!")
                        return kasutajanimi    
                    print("Vale parool")
                    if input("Proovi uuesti? (y/n):").lower()=="y":
                        continue
                    else:
                        return False
        print("Kasutaja ei leidnud")
        if input("Proovi uuesti? (y/n)").lower()=="y":
            continue
        else:
            return False
        

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
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_mail, emailkeywords)
        server.send_message(msg)
    except:
        print("Viga, email pole saadetud")
    finally:
        return True
        print("Email oli saadetud")
        server.quit()
    
def unustanud_parooli_taastamine()->any:
    while True:
        sisend=str(input("Sisesta teie kasutaja nimi või e-posti adress: "))
        find = find_user_data(sisend)
        if find is not None and not find.empty:
            send_mail(find['Kasutaja'],find['Parool'],find['Email'])
            print("Teie parool oli saadetud e-postile: ",find['Email'])
            return True
        if input("Ei leidnud\nProovi uuesti? (y/n): ").lower()=="y":
            continue
        else:
            return False


def oma_andme_muutmine(kasutaja:str)->any:
    find = find_user_data(kasutaja)
    while True:
        s=int(input("Valige mis tahate muutuda (nimi - 1 / email - 2 / parool - 3 / väljuda - 0\n"))
        if s==1:
            while True:
                uusnimi=(str(input("Uus nimi: ")))
                if check_name(uusnimi):
                    if update_user_data(kasutaja, uusnimi, 'Kasutaja', new_username=uusnimi):
                        print("Kasutaja nimi oli muudatud")
                        print(find_user_data(kasutaja))
                    break
                else: continue
        if s==2:
            while True:
                uusemail=(str(input("Uus nimi: ")))
                if check_mail(uusemail):
                    if update_user_data(kasutaja, uusemail, 'Email'):
                        print("Kasutaja email oli muudatud")
                        print(find_user_data(kasutaja))
                    break
                else: continue
        if s==3:
            while True:
                uusparool=(str(input("Uus uusparool: ")))
                if check_password(uusparool):
                    if update_user_data(kasutaja, uusparool, 'Parool'):
                        print("Kasutaja parool oli muudatud")
                        print(find_user_data(kasutaja))
                        break
                else: continue
        if s==0:
            break
        else:
            continue

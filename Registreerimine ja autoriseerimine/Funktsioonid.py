import string
import random
import smtplib,ssl
from email.message import EmailMessage
import os
import pandas as pd

def start():
    if os.path.exists('kasutajate_andmed.csv'):
        return ("Andme fail on juba olemas")
    else:
        data_template = pd.DataFrame({
            'Kasutaja': ["1"],
            'Email': ["1"],
            'Parool': ["1"]
        })
        data_template.to_csv('kasutajate_andmed.csv', index=False)
        return ("Uus andme fail loodud")

def salasona_genereerimine()->str:
    """
    Funktsioon genereerib juhuslik parool. Tagastab genereeritud parool
    param pw: Sisestab genereeritud parool
    """
    pw=''
    for i in range(12):
        t=random.choice(string.ascii_letters) 
        num=random.choice([1,2,3,4,5,6,7,8,9,0])
        t_num=[t,str(num)]
        pw+=random.choice(t_num)
    pw+=random.choice("!@#$%^&*")
    return pw

def check_name(name)->any:
    """
    Funktsioon kontrollib kas nimi pikkus on vastuvõetav, tagastab True või False
    param name: Sisestab nimi
    """
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
    """
    Funktsioon kontrollib kas parool on sisestab erinevad sümbolid. Tagastab True või False
    param password: Sisestab parool
    """
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
    """
    Funktsioon teostab registreerimist ja lisab andmed failisse. 
    Funktsioon kasutab funktsioon find_user_name et alla laadida andmed failist ja kontrollida et kasutaja nimi ei ole hõivatud.
    Kasutab funktsioon email et kontrollida kas emaili vormingus on õige.
    Kasutab funktsioon user_to_file_by_template et kirjutada andmed failis.
    Kasutab funktsioon check_password et kontrolida kas parool vastab kõige nõuetele.

    :param username: Sisestab nimi
    :param find: Sisestab kasutaja andmed (DataFrame)
    :param email: Sisestab kasutaja email.
    :param password: Sisestab kasutaja parool
    """
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
                    user_to_file_by_template(username,email,pw)
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
    """
    Funktsioon tegistab autoriseerimine. Tagastab True või False et kontrollida kas autoriseerimine oli edukalt.
    Funktsioon kasutab funktsioon find_user_name et alla laadida andmed failist ja kontrollida et kasutaja nimi ei ole hõivatud.
    Kasutab funktsioon check_password et kontrolida kas parool vastab kõige nõuetele.

    :param kasutajanimi: Sisestab soovitud kasutajanimi
    :param find: Sisestab kasutaja andmed (DataFrame)
    :param parool: Sisestab kasutaja parool.

    """
    while True:
        kasutajanimi=str(input("Kasutaja nimi: "))
        find = find_user_data(kasutajanimi)
        if find is not None and not find.empty:
            if find['Kasutaja']==kasutajanimi:
                for i in range(3):
                    if i==3: return False
                    parool=str(input("Parool: "))
                    if find['Parool']==parool:
                        print("Sisselogimine on edukalt!")
                        return kasutajanimi
                    print(f"{3-(i+1)}/3 katset jäänud.")
                    continue
                return False
            print("Kasutaja ei leidnud")
            if input("Proovi uuesti? (y/n)").lower()=="y":
                continue
            else:
                return False
        else:
            print("Kasutaja ei leidnud")
            if input("Proovi uuesti? (y/n)").lower()=="y":
                continue
            else:
                return False
            
        

def send_mail(kasutaja:str, password:str, email:str)->any:
    """
    Funktsioon saadab kasutaja andmed ja saadab kasutaja parool emailile. Tagastab True või False et kontrollida kas email oli saadetud.
    """
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
        print("Email oli saadetud")
        server.quit()
        return True
    
def unustanud_parooli_taastamine()->any:
    """
    Funktsioon võimaldab taastada parooli kasutades kasutaja nime või parool. Tagastab True või False.
    Funktsioon kasutab funktsioon find_user_name et alla laadida andmed failist ja kontrollida kas on olemas sisestatud andmed andmebaasis.

    :param sisend: Sisaldab kasutajatele sisestatud andmeid
    :param find: Sisestab kasutaja andmed (DataFrame)
    """
    while True:
        sisend=str(input("Sisesta teie kasutaja nimi või e-posti adress: "))
        find = find_user_data(sisend)
        if find['Kasutaja']==sisend or find['Email']==sisend:
            send_mail(find['Kasutaja'],find['Parool'],find['Email'])
            print("Teie parool oli saadetud e-postile: ",find['Email'])
            return True
        if input("Ei leidnud\nProovi uuesti? (y/n): ").lower()=="y":
            continue
        else:
            return False

def oma_andme_muutmine(kasutaja:str)->any:
    """
    Funktsioon võimaldab muuta kasutaja andmeid, kes seda funktsiooni kasutab.
    Funktsioon kasutab funktsioon update_user_data, et uuendada kasutaja andmeid.

    :param uusnimi: Sisestab uus kasutaja nimi
    :param uusemail: Sisestab uus email
    :param uusparool: Sisestab uus parool
    """
    while True:
        s=int(input("Valige mis tahate muutuda (nimi - 1 / email - 2 / parool - 3 / väljuda - 0\n"))
        if s==1:
            while True:
                uusnimi=str(input("Uus nimi: "))
                if check_name(uusnimi):
                    if update_user_data(kasutaja, uusnimi, 'Kasutaja', new_username=True):
                        print("Kasutaja nimi oli muudatud")
                        kasutaja=uusnimi
                        break
                else: 
                    if input("Proovi uuesti? (y/n):")=="y": continue
                    else: break
        if s==2:
            while True:
                uusemail=(str(input("Uus email: ")))
                if check_mail(uusemail):
                    if update_user_data(kasutaja, uusemail, 'Email'):
                        print("Kasutaja email oli muudatud")
                        break
                else: 
                    if input("Proovi uuesti? (y/n):")=="y": continue
                    else: break
        if s==3:
            while True:
                uusparool=(str(input("Uus uusparool: ")))
                if check_password(uusparool):
                    if update_user_data(kasutaja, uusparool, 'Parool'):
                        print("Kasutaja parool oli muudatud")
                        break
                else: 
                    if input("Proovi uuesti? (y/n):")=="y": continue
                    else: break
        if s==0:
            break
        else:
            continue

def näita_koik_kasutajate_andmed()->any:
    """
    Funktsioon näitab kõiki andmeid failist
    """
    print(pd.read_csv('kasutajate_andmed.csv'))

def user_to_file_by_template(kasutaja, email, pw):
    """
    Funktsioon võimaldab salvestada uue kasutaja andmed faili, kui faili ei ole see loob uue faili.

    :param filename: Sisestab faili nimi, kus asuvad kasutajate andmed.
    :param data_template: Sisestab mall et kirjutada uus kasutaja failisse.
    :param kasutaja: Sisestab kasutajanimi
    :param email: Sisestab email
    :param parool: Sisestab parool.
    """
    filename = 'kasutajate_andmed.csv'
    data_template = pd.DataFrame({
        'Kasutaja': [kasutaja],
        'Email': [email],
        'Parool': [pw]
    })
    if os.path.exists(filename):
        data_template.to_csv(filename, mode='a', header=False, index=False)
    else:
        data_template.to_csv(filename, index=False)

def find_user_data(data):
    """
    Funktsioon otsib antud kasutaja andmed failis ja kõik kasutaja andmed kelle andmed leiab.
    
    :param user_data: Põhjustab leitud andmete salvestamise konteineri
    :param find: Lugege komadega eraldatud väärtuste (csv) faili DataFrame'i.
    """
    file=pd.read_csv('kasutajate_andmed.csv')
    user_data=pd.DataFrame(columns=file.columns)
    for index, row in file.iterrows():
        for c in file.columns:
            if data in str(row[c]):
                user_data = pd.concat([user_data, row.to_frame().T], ignore_index=True)
                break
    if user_data.empty:
        print()
    else:
        return user_data.iloc[0]
    
def update_user_data(kasutaja, new_data, change, new_username=False):
    """
    Funktsioon võimaldab uuenda olulist kasutajate anmed.
    Tagastab True või False.

    :param filename: Sisestab andmefaili nimi
    :param kasutaja: Sisestab kasutaja nimi, kes anmed muutume.
    :param newdata: Sisestab uus andmed mis vaja kirjutada failis.
    :param change: Sisestab kasutaja andmete kategooria nimi, mida tahame muuta
    """
    try:
        filename = 'kasutajate_andmed.csv'
        file = pd.read_csv(filename)
        if kasutaja not in file['Kasutaja'].values:
            print(f"Kasutaja {kasutaja} ei leidnud.")
            return False
        if change in file.columns:
            if new_username is not False:
                file.loc[file['Kasutaja'].str.strip() == kasutaja, 'Kasutaja'] = new_data
                file.to_csv(filename, index=False)
                return True
            if change != 'Kasutaja':
                file.loc[file['Kasutaja'].str.strip() == kasutaja, change] = new_data
                file.to_csv(filename, index=False)
                return True
            else:
                print("fail")
                return False
    except: 
        print("except")
        return False

#1

def arithmetic(arv1:float,arv2:float,tehe:str)->any:
    """Funktsioon kahe arvuga toimingute tulemus.
    :param float arv1: Sisestab esimene arv.
    :param float arv2: Sisestab teine arv.
    :param str tehe: Sisestab matemaatiline tehe märk.
    :param tulemus: Sisestab 
    """
    try:
        if tehe == "+":
            tulemus = arv1 + arv2
        elif tehe == "-":
            tulemus = arv1 - arv2
        elif tehe == "*":
            tulemus = arv1 * arv2
        elif tehe == "/":
            if arv2 != 0:
                tulemus = arv1 / arv2
            else:
                print("Nulliga jagamine ei ole lubatud.")
                exit(0)
        return float(tulemus)
    except:
        return "Vale sisend"

#2
def is_year_leap(year:int)->bool:
    """Funktsioon võtab 1 argumendi – aasta ja tagastab tõene, kui aasta on liigaasta, või False muul juhul.
    :param int year: Sisaldab sisestatud aasta.
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    
#3
import math
def square(side:float)->float:
    """ Funktsioon võtab ühe väärtuse - ruudu külg tagastab 3 väärtust: perimeeter, pindala ja diagonaal
    :param float side: Sisaldab ruudu külje
    :param peri: Sisaldab ruudu perimeeter
    :param sq: Sisaldab ruudu pindala
    :param diag: Sisaldab ruudu diagonaal
    """
    peri=side*4
    sq=side*side
    diag=side*math.sqrt(2)
    return peri,sq,round(diag,2)

#4
def season(month:int)->str:
    """ Funktsioon võtab ühe väärtuse - kalendrikuu number ja tagastab mis aastaaega see kuulub.
    :param int month: Sisaldab kuu number.
    """
    try:
        month=int(month)
        if month>0 and month<13:
            if month in [12, 1, 2]:
                month="Talv" 
            elif month in [3, 4, 5]:
                month="Kevad"
            elif month in [6, 7, 8]:
                month="Suvi"
            elif month in [9, 10, 11]:
                month="Sügis"
        else: month="Vale andmed"
        return month
    except: 
        return "Vale andmed"
    
#5
def bank(a:int, years:int)->any:
    """ Funktsioon sisestab raha sissemakse summa ja aastate arv, mille jooksul nad panka jäävad.
    :param int a: Sisestab raha sissemakse summa
    :param int years: Sisestab aastate arv
    """
    try:
        a=int(a)
        years=int(years)
        prots = 0.10
        for i in range(years):
            a += a * prots
        return a
    except:
        return "Vale andmed"


#6
def is_prime(n:int)->bool:
    """ Funktsioon sisestab üks arv, kontrollib, kas arv on algarv ja tagastab True või False.
    :param int n: Sisestab kontrollitud arv
    """
    while True:
        try:
            n=int(n)
            if n <= 1:
                return False
                break
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
                return True
                break
        except: return "Vale andmed"

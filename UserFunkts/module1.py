import re
import math

#1

def arithmetic(arv1:float,arv2:float,tehe:str)->any:
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
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    
#3
def square(side):
    peri=side*4
    sq=side*side
    diag=side*math.sqrt(2)
    return peri,sq,round(diag,2)

#4
def season(month:int)->any:
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
def bank(a, years):
    try:
        a=int(a)
        years=int(years)
        prots = 0.10
        for i in range(years):
            a += a * prots
        return a
    except:
        return "Vale andmed"


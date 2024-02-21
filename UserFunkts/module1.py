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
    except: return("Vigane tehe")

import re
def checktype(x)->str:
    return str(type(x)).split("'")[1]

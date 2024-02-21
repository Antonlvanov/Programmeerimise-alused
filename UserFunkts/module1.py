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
                print("nulliga jagamine ei ole lubatud.")
                exit(0)
        return float(tulemus)   
    except: return("vigane tehe")
 

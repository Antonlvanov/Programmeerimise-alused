import random
# Genereerime arvu 1 kuni 100
arvuti_arv = random.randint(1, 100) 
while True:
    # Kasutaja arvab arvu ära
    sisend = input("Sisesta oma arv: ") 
    # Sisendi tüüpi kontroll
    try: 
        kasutaja_arv = int(sisend) 
    except ValueError:
        print("Palun sisesta ainult arvud.")
        continue
    # Kahe saadud arvu võrdlus
    if kasutaja_arv == arvuti_arv: 
        print("Õige arv! Palju õnne, võitsid mängu!")
        break
    elif kasutaja_arv < arvuti_arv: 
        print("Proovi suuremat arvu.")
    else:
        print("Proovi väiksemat arvu.")



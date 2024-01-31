import random
arvuti_arv = random.randint(1, 100) 
while True:
    sisend = input("Sisesta oma arv: ")
    try:
        kasutaja_arv = int(sisend)
    except ValueError:
        print("Palun sisesta ainult arvud.")
        continue
    if kasutaja_arv == arvuti_arv:
        print("Õige arv! Palju õnne, võitsid mängu!")
        break
    elif kasutaja_arv < arvuti_arv:
        print("Proovi suuremat arvu.")
    else:
        print("Proovi väiksemat arvu.")



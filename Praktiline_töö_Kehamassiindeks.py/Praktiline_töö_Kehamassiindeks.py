print("Tere! Olen sinu uus sõber - Python!")

nimi=input("Palun sisestage oma nimi. ")
if nimi.isdigit():
    print("Viga! Palun sisestage kehtiv nimi. ")
else:
    print(nimi+", oi kui ilus nimi!")
    number=int(input("! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    if number==1 :
        try:
            pikkus=float(input("Palun sisestage oma pikkus. "))
            pikkus==0
        except ValueError:
            print("Viga! Palun sisestage kehtiv number.")
        try:
            mass=float(input("Palun sisestage oma kaal. "))
        except ValueError:
            print("Viga! Palun sisestage kehtiv number.")
        index=round(mass/(0.01*pikkus)**2,1)
        print(nimi+"! Sinu keha indeks on: "+str(index))
        if index<=16:
            print("Tervisele ohtlik alakaal")
        elif 16>=index<19:
            print("Alakaal")
        elif 19>=index<25:
            print("Normaalkaal")
        elif 25>=index<30:
            print("Ülekaal")
        elif 30>=index<35:
            print("Rasvumine")
        elif 35>=index<40:
            print("Tugev rasvumine")
        elif 40>=index:
            print("Tervisele ohtlik rasvumine")
    if number==0 :
        print("Kahju! See on väga kasulik info!""\n")
        print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")
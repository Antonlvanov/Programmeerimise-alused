from datetime import *
from random import *

# 1
eesnimi = input("sisesta eesnimi: ")
if eesnimi.lower() == "juku":
    vanus = int(input("sisesta vanus: "))
    if 0<vanus<6:
        print("pilet on tasuta.")
    elif 6<=vanus<=14:
        print("lastepilet.")
    elif 15<=vanus<=65:
        print("täispilet.")
    elif vanus>65:
        print("sooduspilet.")
    else:
        print("vigane vanus.")
else:
    print(f"ei saa kinno minna.")

# 2
nimi1=input("sisesta esimese inimese nimi: ")
nimi2=input("sisesta teise inimese nimi: ")
print(f"{nimi1} ja {nimi2} on täna pinginaabrid.")

# 3
a=float(input("sisesta toa esimese seina pikkus: "))
b=float(input("sisesta toa teise seina pikkus: "))
pindala=a*b
print(f"toa pindala on {pindala} ruutmeetrit.")

vastus=input("kas soovid remonti teha (jah/ei)? ").lower()
if vastus=="jah":
    hind=float(input("sisesta põranda ruutmeetri hind: "))
    remondi_maksumus = pindala*hind
    print(f"remondi maksumus on {remondi_maksumus} eurot.")
else:
    print("remonti ei tehta.")

# 4
hind = float(input("sisesta hind: "))
if hind>700:
    allhindlus_hind = hind*0.7
    print(f"30% allahindlusega hind on {allahindlus_hind} eurot.")
else:
    print("hind ei ületa 700 eurot, allahindlust ei anta.")

# 5
temp = float(input("sisesta temperatuur: "))
if temp>18:
    print("temperatuur on üle 18 kraadi.")
elif temp<18:
    print("temperatuur on alla 18 kraadi.")

# 6
pikkus=float(input("inimese pikkus: "))
if pikkus<120:
    print("inimene on lühike.")
elif 120<=pikkus<180:
    print("inimene pikk on keskmine.")
else:
    print("inimene on pikk.")

# 7
pikkus=float(input("sisesta inimese pikkus: "))
sugu=input("sisesta inimese sugu (m/n): ").lower()
if sugu == "n":
    if pikkus<150:
        print("inimene on lühike.")
    elif 150<=pikkus<165:
        print("inimene pikk on keskmine.")
    else:
        print("inimene on pikk.")
else:
    if pikkus < 160:
        print("inimene on lühike.")
    elif 160 <= pikkus < 180:
        print("inimene on keskmise pikkusega.")
    else:
        print("inimene on pikk.")

# 8
arve_nr=datetime.today()#datetime.now()
print(arve_nr)
tsekk="arve: "+str(arve_nr)+"\ntoode hind kogus summa\n"
summa=0

toode="piim"
hind=randint(50,100)/100
v=input("toode: "+toode+ " hind: "+str(hind)+"\nkas tahad osta? ").lower()
if v=="jah":
   mitu=int(input("mitu? "))
   tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
   summa+=mitu*hind
toode="leib"
hind=randint(90,300)/100
v=input("toode: "+toode+ " hind: "+str(hind)+"\nkas tahad osta? ").lower()
if v=="jah":
   mitu=int(input("mitu? "))
   tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
   summa+=mitu*hind
toode="sai"
hind=randint(600,1500)/100
v=input("toode: "+toode+ " hind: "+str(hind)+"\nkas tahad osta? ").lower()
if v=="jah":
   mitu=int(input("mitu? "))
   tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
   summa+=mitu*hind
tsekk+="kokku maksta: "+str(summa)
print(tsekk)
raha=float(input("maksa: " +str(summa) +"\n"))
if raha==summa:
   print("tänan ostu eest!")
if raha>summa:
   print("tänan ostu eest! tagasi " +str(raha-summa))

# 9
a = float(input("sisesta ruudu küljepikkus #1: "))
b = float(input("sisesta ruudu küljepikkus #2: "))
if a==b:
    print("see võib olla ruut.")
else:
    print("see ei saa olla ruut, kuna küljed peavad olema ühepikkused.")

# 10
arv1 = float(input("sisesta esimene arv: "))
arv2 = float(input("sisesta teine arv: "))
tehe = input("sisesta tehe (+, -, *, /): ")

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
else:
    print("vigane tehe.")

print(f"tulemus: {tulemus}")

#11
ta=datetime.today().year
sp=datetime(int(input("sünniasta: ")),int(input("sünnikuu: ")),int(input("sünnipäev: "))).year
if (ta-sp)%5==0:
   print("juubel")
else:
   print("tavaline sünnipäev")

#12 
toote_hind = float(input("sisesta toote hind: "))

if toote_hind <= 10:
    soodustus_protsent = 10
else:
    soodustus_protsent = 20
    
soodustus_hind = toote_hind * (soodustus_protsent / 100)
lopplik_hind = toote_hind - soodustus_hind

print(f"soodustus: {soodustus_protsent}%, lõplik hind: {lopplik_hind} eurot.")

#13 
sugu = input("sisesta sugu (m/n): ").lower()
if sugu == "m":
    vanus = int(input("sisesta vanus: "))
    if 16 <= vanus <= 18:
        print("kandideerija sobib jalgpallimeeskonda.")
    else:
        print("kandideerija ei sobi jalgpallimeeskonda.")
else:
    print("kandideerija ei sobi jalgpallimeeskonda.")

#14
maht=int(input("bussi maht: "))
i=int(input("inimeste arv: "))
ba=round(i/maht) #2,3->2
if i%maht!=0:
   ba+=1
vb=i%maht
print("kokku on vaja {0} bussi ja viimasel sõidavad {1} inimest.".format(ba,vb))

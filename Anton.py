from datetime import *
from random import *
# eesnimi = input("Sisesta eesnimi: ")
# if eesnimi.lower() == "juku":
#     vanus = int(input("Sisesta vanus: "))
#     if 0<vanus<6:
#         print("pilet on tasuta.")
#     elif 6<=vanus<=14:
#         print("lastepilet.")
#     elif 15<=vanus<=65:
#         print("täispilet.")
#     elif vanus>65:
#         print("sooduspilet.")
#     else:
#         print("Vigane vanus.")
# else:
#     print(f"Ei saa kinno minna.")

# # 2
# nimi1=input("Sisesta esimese inimese nimi: ")
# nimi2=input("Sisesta teise inimese nimi: ")
# print(f"{nimi1} ja {nimi2} on täna pinginaabrid.")

# # 3
# a=float(input("Sisesta toa esimese seina pikkus: "))
# b=float(input("Sisesta toa teise seina pikkus: "))
# pindala=a*b
# print(f"Toa pindala on {pindala} ruutmeetrit.")

# vastus=input("Kas soovid remonti teha (jah/ei)? ").lower()
# if vastus=="jah":
#     hind=float(input("Sisesta põranda ruutmeetri hind: "))
#     remondi_maksumus = pindala*hind
#     print(f"Remondi maksumus on {remondi_maksumus} eurot.")
# else:
#     print("Remonti ei tehta.")

# # 4
# hind = float(input("Sisesta hind: "))
# if hind>700:
#     allhindlus_hind = hind*0.7
#     print(f"30% allahindlusega hind on {allahindlus_hind} eurot.")
# else:
#     print("Hind ei ületa 700 eurot, allahindlust ei anta.")

# # 5
# temp = float(input("Sisesta temperatuur: "))
# if temp>18:
#     print("Temperatuur on üle 18 kraadi.")
# elif temp<18:
#     print("Temperatuur on alla 18 kraadi.")

# # 6
# pikkus=float(input("Inimese pikkus: "))
# if pikkus<120:
#     print("Inimene on lühike.")
# elif 120<=pikkus<180:
#     print("Inimene pikk on keskmine.")
# else:
#     print("Inimene on pikk.")

# # 7
# pikkus=float(input("Sisesta inimese pikkus: "))
# sugu=input("Sisesta inimese sugu (m/n): ").lower()
# if sugu == "n":
#     if pikkus<150:
#         print("Inimene on lühike.")
#     elif 150<=pikkus<165:
#         print("Inimene pikk on keskmine.")
#     else:
#         print("Inimene on pikk.")
# else:
#     if pikkus < 160:
#         print("Inimene on lühike.")
#     elif 160 <= pikkus < 180:
#         print("Inimene on keskmise pikkusega.")
#     else:
#         print("Inimene on pikk.")

## 8
## 8.1
#arve_nr=date.today()#datetime.now()
#print(arve_nr)
#tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0

#toode="Piim"
#hind=randint(50,100)/100
#v=input("Toode: "+toode+ " Hind: "+str(hind)+"\nKas tahad osta? ").lower()
#if v=="jah":
#    mitu=int(input("Mitu? "))
#    tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#    summa+=mitu*hind
#toode="Leib"
#hind=randint(90,300)/100
#v=input("Toode: "+toode+ " Hind: "+str(hind)+"\nKas tahad osta? ").lower()
#if v=="jah":
#    mitu=int(input("Mitu? "))
#    tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#    summa+=mitu*hind
#toode="Sai"
#hind=randint(600,1500)/100
#v=input("Toode: "+toode+ " Hind: "+str(hind)+"\nKas tahad osta? ").lower()
#if v=="jah":
#    mitu=int(input("Mitu? "))
#    tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#    summa+=mitu*hind
#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)
#raha=float(input("Maksa: " +str(summa)))
#if raha==summa:
#    print("Tänan ostu eest!")
#if raha>summa:
#    print("Tänan ostu eest! Tagasi " +str(raha-summa))

##8.2 Poes
#arve_nr = date.today()#datetime.now()
#print(arve_nr)
#tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0
#for toode in {"Piim, Leib, Sai"}:
#    hind=randint(50,100)/100
#    v=input("Toode: "+toode+ " Hind: "+str(hind)+"\nKas tahad osta?").lower()
#    if v=="jah":
#        mitu=int(input("Mitu? "))
#        tsekk+=toode+"  "+str(hind)+"  "+str(mitu)+"  "+str(mitu*hind)+"\n"
#        summa+=mitu*hind
#tsekk="Kokku maksta: " +str(summa)
#print(tsekk)
#while True:
#    raha=float(input("Maksa "+str(summa)+"\n"))
#    if raha==summa:
#        print("Tänan ostu eest!")
#        break
#    elif raha>summa:
#        print("Tänan ostu eest! Tagasi "+str(raha-summa))
#        break
#    else:
#        summa-=raha
#        print("Maksa veer"+str(summa))
    
##11
#ta.date.today().year
#sp.date(int(input("Sünniasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: "))).year
#if (ta-sp)%5==0:
#    print("Juubel")
#else:
#    print("Tavaline sünnipäev")

##11
#ta.date.today().year
#sp.date(int(input("Sünniasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: "))).year
#if (ta-sp)%5==0:
#    print("Juubel")
#else:
#    print("Tavaline sünnipäev")

##14
#maht=int(input("Bussi maht: "))
#i=int(input("Inimeste arv: "))
#ba=round(i/maht) #2,3->2
#if i%maht!=0:
#    ba+=1
#vb=i%maht
#print("Kokku on vaja {0} bussi ja viimasel sõidavad {1} inimest".format(ba,vb))
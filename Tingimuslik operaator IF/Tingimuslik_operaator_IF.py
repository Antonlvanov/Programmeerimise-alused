# �lesanne 1 - Juku
eesnimi = input("Sisesta eesnimi: ")

if eesnimi.lower() == "juku":
    vanus = int(input("Sisesta vanus: "))
    if 0 < vanus < 6:
        print("pilet on tasuta.")
    elif 6 <= vanus <= 14:
        print("lastepilet.")
    elif 15 <= vanus <= 65:
        print("t�ispilet.")
    elif vanus > 65:
        print("sooduspilet.")
    else:
        print("Vigane vanus.")
else:
    print(f"{eesnimi} ei saa Jukuga kinno minna.")

# �lesanne 2 - Pinginaabrid
nimi1 = input("Sisesta esimese inimese nimi: ")
nimi2 = input("Sisesta teise inimese nimi: ")
print(f"{nimi1} ja {nimi2} on t�na pinginaabrid.")

# �lesanne 3 - Remont
pikkus = float(input("Sisesta ristk�likukujulise toa esimese seina pikkus: "))
laius = float(input("Sisesta ristk�likukujulise toa teise seina pikkus: "))
pindala = pikkus * laius
print(f"Ristk�likutoa pindala on {pindala} ruutmeetrit.")

remont_soov = input("Kas soovid remonti teha (jah/ei)? ").lower()
if remont_soov == "jah":
    ruutmeetri_hind = float(input("Sisesta ruutmeetri hind: "))
    remondi_maksumus = pindala * ruutmeetri_hind
    print(f"Remondi maksumus on {remondi_maksumus} eurot.")
else:
    print("Remonti ei tehta.")

# �lesanne 4 - Allahindlus
alghind = float(input("Sisesta alghind: "))
if alghind > 700:
    allahindlus_hind = 0.7 * alghind
    print(f"30% allahindlusega hind on {allahindlus_hind} eurot.")
else:
    print("Alghind ei �leta 700 eurot, allahindlust ei anta.")

# �lesanne 5 - Temperatuur
temperatuur = float(input("Sisesta temperatuur: "))
if temperatuur > 18:
    print("Temperatuur on �le 18 kraadi, soovitav toasoojus talvel.")

# �lesanne 6 - Pikkus
pikkus = float(input("Sisesta inimese pikkus: "))
if pikkus < 160:
    print("Inimene on l�hike.")
elif 160 <= pikkus < 180:
    print("Inimene on keskmise pikkusega.")
else:
    print("Inimene on pikk.")

# �lesanne 7 - Pikkus ja sugu
pikkus = float(input("Sisesta inimese pikkus: "))
sugu = input("Sisesta inimese sugu (m/n): ").lower()

if sugu == "n":
    print("Naised ei vaja pikkuse j�rgi hindamist.")
else:
    if pikkus < 160:
        print("Inimene on l�hike.")
    elif 160 <= pikkus < 180:
        print("Inimene on keskmise pikkusega.")
    else:
        print("Inimene on pikk.")

# �lesanne 8 - Poes
tooted = {"piim": 1.5, "saia": 0.8, "leiba": 1.2}  # Lisa siia rohkem tooteid
kogusumma = 0

for toode, hind in tooted.items():
    kogus = int(input(f"Mitu t�kki {toode} soovid osta? "))
    kogusumma += kogus * hind
    print(f"{toode}: {kogus} t�kki x {hind} eurot/t�kk = {kogus * hind} eurot")

print(f"Kogusumma: {kogusumma} eurot.")

# �lesanne 9 - Ruut
kylg = float(input("Sisesta ruudu k�ljepikkus: "))
if kylg > 0:
    print("See v�ib olla ruut.")
else:
    print("See ei saa olla ruut, sest k�ljepikkus peab olema suurem kui 0.")

# �lesanne 10 - Matemaatika
arv1 = float(input("Sisesta esimene arv: "))
arv2 = float(input("Sisesta teine arv: "))
tehe = input("Sisesta tehe (+, -, *, /): ")

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
else:
    print("Vigane tehe.")

print(f"Tulemus: {tulemus}")

# �lesanne 11 - Juubel
sunnipaev = int(input("Sisesta s�nnip�eva aasta: "))
juubel_aastad = [50, 60, 70, 80, 90, 100]
if 2024 - sunnipaev in juubel_aastad:
    print("See on juubeliaasta!")
else:
    print("See ei ole juubeliaasta.")

# �lesanne 12 - M��k
toote_hind = float(input("Sisesta toote hind: "))

if toote_hind <= 10:
    soodustus_protsent = 10
else:
    soodustus_protsent = 20

soodustus_hind = toote_hind * (soodustus_protsent / 100)
lopplik_hind = toote_hind - soodustus_hind

print(f"Soodustus: {soodustus_protsent}%, L�plik hind: {lopplik_hind} eurot.")

# �lesanne 13 - Jalgpalli meeskond
vanus = int(input("Sisesta vanus: "))
sugu = input("Sisesta sugu (m/n): ").lower()

if 16 <= vanus <= 18 and sugu == "m":
    print("Kandideerija sobib jalgpallimeeskonda.")
else:
    print("Kandideerija ei sobi jalgpallimeeskonda.")

# �lesanne 14 - Busside logistika
inimesed = int(input("Sisesta inimeste arv: "))
bussi_kohad = int(input("Sisesta bussi kohtade arv: "))

busside_arv = inimesed // bussi_kohad
viimases_bussis = inimesed % bussi_kohad

print(f"Vajalike busside arv: {busside_arv}")
print(f"Inimesi viimases bussis: {viimases_bussis}")

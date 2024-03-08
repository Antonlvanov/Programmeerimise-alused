from os import system
from gtts import *
def loe_failist(fail:str):
    """Loeme failist ja salvestame järjendisse. Funktsioon tagastab järjend
    :param str fail:
    :rtype: list
    """
    try:
        f=open(fail,'r',endcoding="utf-8") #try
        jarjend=[]
        for rida in f:
            jarjend.append(rida.strip())
        f.close()
        return jarjend
    except Exception as e:
        print(e)

def kirjuta_failisse(fail:str,jarjend=[]):
    """
    """
    for i in range(len(jarjend)):
        jarjend.append(input(f"{i+1} element: "))
    f=open(fail,'w',encoding="utf-8")
    for el in jarjend:
        f.write(el+"\n")
    f.close()

def heli(tekst:str,keel:str):
    obj=gTTS(text=tekst,lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")

tekst=input("Sisesta tekst: ")
heli(tekst,'et')

kirjuta_failisse("Fail.txt")

#paevad=loe_failist("Fail.txt")
#print(paevad)
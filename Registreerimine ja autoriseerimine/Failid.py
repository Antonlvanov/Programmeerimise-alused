from module1 import *
from os import system
from gtts import *
import pandas as pd

def template():
    template_df = pd.DataFrame({
        'Username': [],
        'Email': [],
        'Phone': [],
        'Address': []
    })
    template_df.to_csv('users_template.csv', index=False)
    
def loe_failist(kasutaja_info:str,kasutajad:list,paroolid:list,emailid:list)->any:
    """Loeme failist ja salvestame järjendisse. Funktsioon tagastab järjend
    :param str fail:
    :rtype: list
    """
    try:
        f=open(fail,'r',endcoding="utf-8") #tryw 
        jarjend=[]
        for rida in f:
            jarjend.append(rida.strip())
        f.close()
        return jarjend
    except Exception as e:
        print(e)

def kirjuta_failisse(fail:str,kasutajad:list,paroolid:list,emailid:list):
    """
    """
    for i in range(len(jarjend)):
        jarjend.append(input(f"{i+1} element: "))
    f=open(fail,'w',encoding="utf-8")
    for el in jarjend:
        f.write(el+"\n")
    f.close()

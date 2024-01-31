##1
#userinput = input("Sisesta jõulupuu arv 1-9: ")
#try:
#    kasutaja_arv = int(userinput)
#except ValueError:
#    print("Palun sisesta ainult arvud.")
#esi1="   /V\    "
#esi2="   /V\    "
#esi3="   /V\    "
#esi4="   /V\    "
#for i in range(1):
#        print("   /V\    "*kasutaja_arv)
#        print("  / V \   "*kasutaja_arv)
#        print(" / V V \  "*kasutaja_arv)
#        print("/VV V VV\ "*kasutaja_arv)

##2
#R = input("Sisesta arv: ")
#result = 1
#try:
#    kasutaja_arv = int(R)
#except ValueError:
#    print("Palun sisesta ainult arvud.")
#    exit(0)
#if (R%2==0):
#    R-1
#    for i in range(1, R, 2):
#            result *= i
#else:
#    for i in range(1, R, 2):
#            result *= i
#print("Paaritute väärtuste korrutis 0 kuni", R, ":", result)

##3
#import random

#N = random.randint(1, 100)
#print("Genereeritud arvude arv: " +(str(N)))
#numbers = [random.randint(-100, 100) for i in range(N)]
#print("Genereeritud numbrite nimekiri: " + str(numbers))
#p_count=0
#for i in numbers:
#    if i > 0:
#        p_count+=1
#print("Positiivsete numbrite arv nimekirjas: "+ str(p_count))

#4
userinput = input("Sisesta täisarv: ")
try:
    kasutaja_arv = int(userinput)
except ValueError:
    print("Palun sisesta õige arv.")
n_c=0
p_c=0
for i in range (len(str(userinput))):
        string = str(userinput)
        substring = string[i]
        if int(substring)%2==0:
            n_c+=1
        if int(substring)%2!=0:
            p_c+=1
print(f"sisestatud naturaalarvu paarisarv: {p_c}")
print(f"paaritud numbrid sisestatud naturaalarv: {n_c}")  
        
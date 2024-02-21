#1
userinput = input("Sisesta jõulupuu arv 1-9: ")
try:
    kasutaja_arv = int(userinput)
except ValueError:
    print("Palun sisesta ainult arvud.")
for i in range(1):
        print(" ")
        print("    X     "*kasutaja_arv)
        print("   /V\    "*kasutaja_arv)
        print("  / V \   "*kasutaja_arv)
        print(" / V V \  "*kasutaja_arv)
        print("/VV V VV\ "*kasutaja_arv)
        print(" ")

#2
R = input("Sisesta arv: ")
result = 1
try:
    kasutaja_arv = int(R)
except ValueError:
    print("Palun sisesta ainult arvud.")
    exit(0)
if kasutaja_arv%2==0:
    kasutaja_arv-1
for i in range(1, kasutaja_arv+1, 2):
        result *=i
print("Paaritute väärtuste korrutis 0 kuni", kasutaja_arv, ":", result)

#3
import random

N = random.randint(1, 100)
print("Genereeritud arvude arv: " +(str(N)))
numbers = [random.randint(-100, 100) for i in range(N)]
print("Genereeritud numbrite nimekiri: " + str(numbers))
p_count=0
for i in numbers:
    if i > 0:
        p_count+=1
print("Positiivsete numbrite arv nimekirjas: "+ str(p_count))

#4
userinput = input("Sisesta täisarv: ")
try:
    kasutaja_arv = int(userinput)
except ValueError:
    print("Palun sisesta õige arv.")
    exit(0)
n_c=0
p_c=0
for i in range (len(str(userinput))):
        string = str(userinput)
        substring = string[i]
        if int(substring)%2==0:
            n_c+=1
        if int(substring)%2!=0:
            p_c+=1
print(f"Sisestatud naturaalarvu paarisarv: {p_c}")
print(f"Paaritud numbrid sisestatud naturaalarv: {n_c}")  

#5

A=int(input("Sisesta A väärtus: "))
B=int(input("Sisesta B väärtus: "))
if A > B:
    print("Viga: A peab olema väiksem või võrdne B-ga.")
else:
    sum_result = 0
    for num in range(A, B + 1):
        sum_result += num
print(f"Astme summa A kuni B: {sum_result}")       

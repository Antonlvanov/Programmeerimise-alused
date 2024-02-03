#1
#for
count=0
for i in range(15):
    arv=float(input("sisesta {0} arv: ".format(i+1)))
    d=0
    if arv==int(arv):
        count+=1
print("Täisarvude arv on "+str(count))

# #while true
# r=0
# i=0
# while true:
#     arv=float(input("sisesta {0} arv ".format(i)))
#     i+=1
#     if arv==int(arv):
#         r+=1
#     if i==15: break
# print("täisarvude arv on " +str(r))

# #while tingimustega
# r=0
# i=1
# while i<16:
#     arv=float(input("sisesta {0} arv: ".format(i)))
#     i+=1
#     if arv==int(arv):
#         r+=1
# print("täisarvude arv on " +str(r))

# #2
# a=int(input("sisesta arv: "))
# i=1
# count=0
# while i<a:
#     count+=i
#     i+=1
#     print(count)
# print("summa on: "+str(count))

# #3
# numbers = [float(input("введите число: ")) for i in range(8)]
# count = 1
# for num in numbers:
#     if num > 0:
#         count *= num
# print("Произведение положительных чисел: ", count)

# #4
# for i in range(10, 21):
#     print(i**2)

# #5
# n = int(input("Введите количество чисел: "))
# sum_neg = 0
# for i in range(n):
#     num = float(input("Введите число: "))
#     if num < 0:
#         sum_neg += num
# print("Cумма отрицательных чисел:", sum_neg)

# #6
# N = int(input("Введите количество чисел: "))
# neg = 0
# pos = 0
# zeros = 0
# for i in range(N):
#     num=float(input("Введите число: "))
#     if num < 0:
#         neg += 1
#     elif num > 0:
#         pos += 1
#     else:
#         zeros += 1
# print("\n""Отрицательных:", neg)
# print("Положительных:", pos)
# print("Нулей:", zeros)

# #7
# A = int(input("Введите начало промежутка: "))
# B = int(input("Введите конец промежутка: "))
# K = int(input("Введите K: "))
# for num in range(A, B + 1):
#     if num % K == 0:
#         print(num)

# #8
# for inches in range(1, 21):
#     centimeters = inches * 2.5
#     if inches == 1:
#         print(f"{inches} дюйм = {centimeters:.2f} см")
#     elif 1 < inches < 5:
#         print(f"{inches} дюйма = {centimeters:.2f} см")
#     else:
#         print(f"{inches} дюймов = {centimeters:.2f} см")

# #9
# S = float(input("Введите сумму вклада: "))
# years = int(input("Введите период (в годах): "))
# rate = 0.03
# for i in range(years):
#     S+=S*rate
# print("Через", years, "лет сумма составит:", round(S,2))

# #13
# for i in range(10):
#     num1 = float(input("Введите первое число: "))
#     num2 = float(input("Введите второе число: "))
#     if num1>num2:
#         print("Большее из чисел:", num1)
#     elif num1<num2:
#         print("Большее из чисел:", num2)
#     elif num1==num2:
#         print("Числа равны")
        
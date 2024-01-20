#1
#for
r=0
for i in range(15):
    arv=float(input("sisesta {0} arv: ".format(i+1)))
    d=0
    if arv==int(arv):
        r+=1
print("Täisarvude arv on "+str(r))
# #while True
# r=0
# i=0
# while True:
#     arv=float(input("Sisesta {0} arv ".format(i)))
#     i+=1
#     if arv==int(arv):
#         r+=1
#     if i==15: break
# print("Täisarvude arv on " +str(r))

# #while tingimustega
# r=0
# i=1
# while i<16:
#     arv=float(input("Sisesta {0} arv: ".format(i)))
#     i+=1
#     if arv==int(arv):
#         r+=1
# print("Täisarvude arv on " +str(r))

# #2
# A=int(input("Sisesta arv: "))
# i=1
# count=0
# while i<A:
#     count+=i
#     i+=1
#     print(count)
# print("Summa on: "+str(count))

# # Задание 3
# numbers = [float(input("Введите число: ")) for _ in range(8)]
# product = 1

# for num in numbers:
#     if num > 0:
#         product *= num

# print("Произведение положительных чисел:", product)

# # Задание 4
# for i in range(10, 21):
#     print(i**2)

# # Задание 5
# N = int(input("Введите количество чисел: "))
# sum_negatives = 0

# for _ in range(N):
#     num = float(input("Введите число: "))
#     if num < 0:
#         sum_negatives += num

# print("Сумма отрицательных чисел:", sum_negatives)

# # Задание 6
# N = int(input("Введите количество чисел: "))
# negatives = 0
# positives = 0
# zeros = 0

# for _ in range(N):
#     num = float(input("Введите число: "))
#     if num < 0:
#         negatives += 1
#     elif num > 0:
#         positives += 1
#     else:
#         zeros += 1

# print("Отрицательных:", negatives)
# print("Положительных:", positives)
# print("Нулей:", zeros)

# # Задание 7
# A = int(input("Введите начало промежутка: "))
# B = int(input("Введите конец промежутка: "))
# K = int(input("Введите K: "))

# for num in range(A, B + 1):
#     if num % K == 0:
#         print(num)

# # Задание 8
# for inches in range(1, 21):
#     centimeters = inches * 2.54
#     print(f"{inches} дюймов = {centimeters:.2f} см")

# # Задание 9
# S = float(input("Введите сумму вклада: "))
# N = int(input("Введите количество лет: "))
# interest_rate = 3 / 100

# for _ in range(N):
#     S += S * interest_rate

# print("Сумма вклада через", N, "лет составит:", S)

# # Задание 10
# for _ in range(10):
#     num1 = float(input("Введите первое число: "))
#     num2 = float(input("Введите второе число: "))
    
#     max_number = max(num1, num2)
#     print("Большее из чисел:", max_number)

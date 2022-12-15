# # 2.Задайте натуральное число N. 
# # Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите целое число: "))
my_lst = []   
simple = 2
while num > 1:
    if num % simple == 0:
        my_lst.append(simple)
        num = num/simple
    else:
        simple += 1
print(my_lst)

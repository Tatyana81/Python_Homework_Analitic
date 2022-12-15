# 4.Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# *Пример:* 
#  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = int(input("Введите целое число: "))
my_lst = []
for i in range(1,k+2):
    my_lst.append(random.randint(0, 101)) #формируем список коэффициентов многочлена

print(my_lst) 
polynomial = ''
n = 0

# в зависимости от коэффициента (0 или 1 или другой) формируем строку многочлена
for i in range(0, k+1):
    if i == (k - 1) and my_lst[i] not in (0, 1):                    
        polynomial = polynomial + str(my_lst[i]) + 'x' + ' + ' 
    elif i == (k - 1) and my_lst[i] == 1:                       
        polynomial = polynomial + 'x' + ' + ' 

    elif i != k and my_lst[i] not in (0, 1):                    
        polynomial = polynomial + str(my_lst[i]) + 'x^' + str(k - i) + ' + ' 
    elif i != k and my_lst[i] == 1:
        polynomial = polynomial + 'x^' + str(k - i) + ' + ' 

    elif i == k and my_lst[i] != 0:
        polynomial = polynomial + str(my_lst[i])
    elif i == k and my_lst[i] == 0:
        polynomial = polynomial[:-2] 
    else:
        pass
   
print(polynomial)

with open('polynomial_4_4.txt', 'w') as data:
    data.write(polynomial)


# 5.Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


with open('polynomial_1.txt', 'r') as data:
    f1 = str(data.readlines()) #если считываю без str, то тип получается list
with open('polynomial_2.txt', 'r') as data:
    f2 = str(data.readlines())
    

f1=f1.replace("'", '') # не пойму как считать строку из файла без элементов [, ], '
f1=f1.replace("[", '')
f1=f1.replace("]", '')
f2=f2.replace("'", '') # не пойму как считать строку из файла без элементов [, ], '
f2=f2.replace("[", '')
f2=f2.replace("]", '')

print("Первый многочлен", f1)
print("Второй многочлен", f2)

f1 = f1.split("+")
list1 = []
for i in f1:
    list1.append(int(i.split("x")[0]))

f2 = f2.split("+")
list2 = []
for i in f2:
    list2.append(int(i.split("x")[0]))

my_lst = []
k = 3 #степень многочлена
for i in range(k+1):
    my_lst.append(list1[i] + list2[i])

# в зависимости от коэффициента (0 или 1 или другой) формируем строку многочлена
polynomial = ''
n = 0
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
   
print("Сумма многочленов", polynomial)
with open('polynomial_sum.txt', 'w') as data:
    data.write(polynomial)
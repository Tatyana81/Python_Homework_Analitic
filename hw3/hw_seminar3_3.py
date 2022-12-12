# 3.Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list1=[1.1, 1.2, 3.1, 5, 10.01]
list2=[]

def create_list2(s): #создаем список из дробных частей элементов списка1.
    for i in s:
        if i !='.':
            s=s.lstrip(i)
        else:
            s='1'+s
            break
    list2.append(float(s))

for i in list1:
    if type(i)==int:
        pass
    else: 
        string=str(i)
        create_list2(string)

print(f'Исходный список {list1}')

result=(max(list2)-min(list2)) #выходит ооочень много знаков после запятой. Исправим это. 

#находим наибольшее кол-во элементов после запятой у max и min, чтобы округлить результат до такого же кол-ва
s1 = str(max(list2))
s2 = str(min(list2))
if (abs(s1.find('.') - len(s1)) - 1)>(abs(s2.find('.') - len(s2)) - 1):
    print(round(result,abs(s1.find('.') - len(s1))))
else:
    print(round(result,abs(s2.find('.') - len(s2))))






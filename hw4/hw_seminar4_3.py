# 3.Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример: [2,5,8,2,6,5,9] -> [8,6,9]

# Два решения. Это первое. Ниже второе. 

# my_list = [2,5,8,2,6,5,9]
# list_minus = []
# lots_of_my_list = set(my_list)  # множество из элементов исходного списка

# for i in range(0, len(my_list)-1):     # создаем список из элементов, которые повторяются 
#     for j in range(i+1, len(my_list)):
#         if my_list[i] == my_list[j]:
#             list_minus.append(my_list[i])
#         else:
#             pass
# else:
#     pass

# lots_of_list_minus = set(list_minus) # множество из элементов, которые повторяются
# print(list(lots_of_my_list - lots_of_list_minus))

# Второе решение
slovar = {}
my_list  = [2,5,8,2,6,5,9]
for i in my_list :
  slovar[i] = slovar.get(i, 0) + 1

spisok = []
for key, value in slovar.items():
   if value == 1:
     spisok.append(key)
print(f'Исходный список {my_list}')
print(spisok)





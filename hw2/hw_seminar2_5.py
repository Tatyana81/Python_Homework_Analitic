# Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно)

import random
def mix(my_lst):
    copy_my_lst=my_lst[:]#создаем копию списка
    for i in range(len(copy_my_lst)):
        #получение случайного индекса
        index_mix=random.randint(0, len(copy_my_lst) - 1)
        # Замена
        temp = copy_my_lst[i]
        copy_my_lst[i] = copy_my_lst[index_mix]
        copy_my_lst[index_mix] = temp
    return copy_my_lst
list = [1,2,3,4,5,6,7,8,9]

mixed_list = mix(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)

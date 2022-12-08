# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число. //2 3 5 

n = int(input("Введите целое число: "))
my_lst = []
for x in range(n*(-1), n+1):
     my_lst.append(x)

with open('file.txt', 'r') as data:
    positions = data.readlines() #считываем с файла номера позиций в список

work=1
for i in positions:
        work*=my_lst[int(i)]
       
print (f'Исходный список {my_lst}')

for i in positions:
    print(f' Индекс позиции {(int(i))}')

print (f'Произведение элементов исходного списка на указанных позициях равно {work}')
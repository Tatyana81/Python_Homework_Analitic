# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
import math
num = int(input("Введите целое число: "))
result=''
while num > 1:
    result=str(num%2)+result
    num= num//2
result=str(num)+result
print(result)

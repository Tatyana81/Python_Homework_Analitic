# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
a1 = int(input("введите кординаты X первой точки: "))
b1 = int(input("введите кординаты Y второй точки: "))
a2 = int(input("введите кординаты X первой точки: "))
b2 = int(input("введите кординаты Y второй точки: "))

def distance(number1,number2,number3,number4):
    from math import sqrt
    return sqrt((number3-number1)**2+(number4-number2)**2)
   
print(round(distance(a1,b1,a2,b2) ,3))
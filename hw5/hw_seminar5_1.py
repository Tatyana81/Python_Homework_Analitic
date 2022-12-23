#3. Напишите программу, удаляющую из текста все слова, содержащие "абв"
# абв абвг мой мир ----> мой мир.

with open('words2.txt', 'r') as data:
    words = data.readline()

words = words.split()
x = 'абв'
lis = [i for i in words if x not in i]
print(*lis)


# with open('words.txt', 'w') as data:
#     data.writelines(str(lis))
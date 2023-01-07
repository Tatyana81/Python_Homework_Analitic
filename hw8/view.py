def showmenu():
    print("Выберете действия:\n1- Показать всех сотрудников\n2- Добавить сотрудника\n3- Удалить сотрудника"
          "\n4- Выход")
    select = int(input())
    return select


def add_man():
    print("Введите Имя, Фамилию и номер телефона через пробел ")
    man = input().split()
    return(man)


def delet_menu():
    print("Введите номер записи для удаления ")
    delet = int(input())
    return(delet)


def show_result(msg):
    print(msg)

def show_people(people):
    print("N\tИмя\tФамилия\tНомер телефона\t")
    for i, p in enumerate(people):
        print(i, *p, sep = '\t')









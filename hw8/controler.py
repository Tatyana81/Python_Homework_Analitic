from view import *
from model import *


def main():
    while True:
        select = showmenu()
        if select == 1:
            people = get_people()
            show_people(people)
        elif select == 2:
            man = add_man()
            add(man)
            show_result ("Запись добавлена")
        elif select == 3:
            number = delet_menu()
            delet(number)
            show_result ("Запись удалена")
        elif select == 4:
            show_result ("До встречи")
            break



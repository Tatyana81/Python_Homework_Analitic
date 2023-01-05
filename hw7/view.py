def showmenu():
    print("Выберете действия:\n1- Импорт с тхт\n2- Экспорт в тхт\n3- Импорт с csv\n4- Экспорт в csv")
    select = input()
    return select

def stroki():
    print("Введите новые данные: Фамилия, Имя, Телефон - каждое слово с новой строки")
    new_info = []
    for i in range(3):
        sl = input()
        new_info.append(sl)
    return(new_info)







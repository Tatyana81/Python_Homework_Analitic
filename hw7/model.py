import csv
import view


def import_from_csv():
    with open("classmates.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        # for row in file_reader:
        #     print(row)
        return(list(file_reader))


def export_to_csv():
    with open("classmates1.csv", mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        # row = ['Фамилия', 'Имя', 'Телефон']
        # row1 = ['Иванов', 'Иван', '8876987']
        # file_writer.writerow(row)
        file_writer.writerow(view.stroki())


def import_from_txt():
    with open('classmates.txt','r', encoding = 'utf-8') as data:
        words = data.read()
        return (words)


def export_to_txt():
    with open('classmates.1txt', 'a') as data:
        for j in view.stroki():
            data.write(str(j) + '\n')





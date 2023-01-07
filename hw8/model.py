import csv
# import view

def get_people():
    with open("people.csv", encoding='utf-8') as scvfile:
        reader = csv.reader(scvfile, delimiter=";")
        # title = next(reader)
        sp = list(reader)
        return(sp)
        

def add(man):
    with open("people.csv", 'a', encoding='utf-8', newline='') as scvfile:
        writer = csv.writer(scvfile, delimiter=";")
        writer.writerow(man)


def delet(number):
    with open("people.csv", encoding='utf-8') as scvfile:
        reader = csv.reader(scvfile, delimiter=";")
        sp = list(reader)
    del sp[number]
    with open("people.csv", 'w', encoding='utf-8', newline='') as scvfile:
        writer = csv.writer(scvfile, delimiter=";")
        for row in sp:
            writer.writerow(row)
        

        

# def import_from_csv():
#     with open("classmates.csv", encoding='utf-8') as r_file:
#         file_reader = csv.reader(r_file, delimiter=",")
#         # for row in file_reader:
#         #     print(row)
#         return(list(file_reader))


# def export_to_csv():
#     with open("classmates1.csv", mode="w", encoding='utf-8') as w_file:
#         file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
#         # row = ['Фамилия', 'Имя', 'Телефон']
#         # row1 = ['Иванов', 'Иван', '8876987']
#         # file_writer.writerow(row)
#         file_writer.writerow(view.stroki())


# def import_from_txt():
#     with open('classmates.txt','r', encoding = 'utf-8') as data:
#         words = data.read()
#         return (words)


# def export_to_txt():
#     with open('classmates.1txt', 'a') as data:
#         for j in view.stroki():
#             data.write(str(j) + '\n')





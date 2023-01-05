import view
import model

def main():
    select = view.showmenu()
    if select == "1":
        x = model.import_from_txt()
        print(x)
    if select == "2":
        x = model.export_to_txt()
    if select == "3":
        x = model.import_from_csv()
        print(x)
    if select == "4":
        x = model.export_to_csv()
        print(x)
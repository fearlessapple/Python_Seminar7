from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data

def input_data():
    last_name = input("Введите Фамилию: ")
    first_name = input("Введите Имя: ")
    father_name = input("Введите Отчество: ")
    birth_date = input("Введите Дату рождения: ")
    phone_number = input("Введите Номер контакта: ")
    return [last_name, first_name, father_name, birth_date, phone_number]

def input_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def input_choice():
    print("Выберите необходимое действие: 1 - импорт, 2 - экспорт, 3 - поиск контакта.")
    choice = input("Введите цифру: ")
    if choice == '1':
        sep = input_sep()
        import_data(input_data(), sep)
    elif choice == '2':
        data = export_data()
        print_data(data)
    else:
        word = input("Введите данные для поиска: ")
        data = export_data()
        item = search_data(word, data)
        if item != None:
            print(f"Фамилия: {item[0]}, Имя: {item[1]}, Отчество: {item[2]}, Дата рождения: {item[3]}, Телефон: {item[4]}.")
        else:
            print("Данные не обнаружены.")
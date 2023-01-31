def print_data(data):
    if len(data) > 0:
        for item in data:
            print(f"Фамилия: {item[0]}, Имя: {item[1]}, Отчество: {item[2]}, Дата рождения: {item[3]}, Телефон: {item[4]}.")
    else:
        print("Справочник пуст!")
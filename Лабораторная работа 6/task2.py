import json

INPUT_FILE = "input.csv"


# Вариант 1 без использования функции zip


def csv_to_list_dict1(filename: str) -> list[dict]:
    with open(filename) as f:
        data = f.readlines() # Считал весь текст
        headers_str = data[0].rstrip() # Выделил из текста строку заголовков
        headers_list = [header for header in headers_str.split(',')] # Создал список из строки заголовков
        rows_str = data[1:] # Выделил из текста строки рядов значений
        table = [] # Создал пустой список, в который будут записаны словари типа "заголовок: значение" для каждого ряда
        for row_str in rows_str: # Для каждой строки ряда значений:
            values_list = [value for value in row_str.rstrip().split(',')] # Создал список значений из строки
            # текущего ряда
            values_dict = {} # Создал пустой словарь
            for index, value in enumerate(headers_list): # Для каждого проиндексированного заголовка:
                current_header = headers_list[index] # В явном виде обозначил текущий заголовок
                current_value = values_list[index] # В явном виде обозначил текущее значение ряда, соответствующее
                # текущему заголовку
                values_dict[current_header] = values_dict.get(current_header, current_value) # Занёс текущее значение
                # ряда в словарь по ключу в виде текущего заголовка
            table.append(values_dict) # Добавил составленный словарь типа "заголовок: значение" в список
    return table


# print(json.dumps(csv_to_list_dict1(INPUT_FILE), indent=4))


# Вариант 2 с использованием функции zip


def csv_to_list_dict2(filename: str) -> list[dict]:
    with open(filename) as f:
        data = f.readlines()  # Считал весь текст
        headers_str = data[0].rstrip()  # Выделил из текста строку заголовков
        headers_list = [header for header in headers_str.split(',')]  # Создал список из строки заголовков
        rows_str = data[1:]  # Выделил из текста строки рядов значений
        table = []  # Создал пустой список, в который будут записаны словари типа "заголовок: значение" для каждого ряда
        for row_str in rows_str:  # Для каждой строки ряда значений:
            values_list = [value for value in row_str.rstrip().split(',')]  # Создал список значений из строки
            # текущего ряда
            row_dict = dict(zip(headers_list, values_list)) # Создал словарь типа "заголовок: значение"
            # для текущего ряда
            table.append(row_dict)  # Добавил составленный словарь типа "заголовок: значение" в список
        return table


print(json.dumps(csv_to_list_dict2(INPUT_FILE), indent=4))

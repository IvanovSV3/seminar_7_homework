# Строка содержит id,имя,фамилию,номер телефона, комментрий - символ разделитель на 
# выбор(можно использовать пробел или запятые) + файл с хранением этих строк

def input_data():
    temp = int(input("Выберите:\n 1 - добавить пользователя;\n 2 - Посмотреь пользователей;\n 3 - сортировать по имени;\n 4 - сортировать по id;\n 5 - Выход\n №: "))
    return temp
# print(input_data())

def function_1():
    temp_id = int(input("id - "))
    temp_name = input("Имя ")
    temp_surname = input("Фамилия ")
    temp_telefon = int(input("Телефон - "))
    temp_surname = input("Коммент ")
    lene = [temp_id, temp_name, temp_surname, temp_telefon, temp_surname]
    lene_str = ",".join(map(str, lene))
    # print(lene)
    # return lene
    with open("work_list.txt", "a") as file:
        file.write(lene_str + '\n')
    print('save')

def function_2():
    with open("work_list.txt", "r") as file:
        for line in file.readlines():
            print(line, end="")
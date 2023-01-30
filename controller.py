# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных.
# Модуль контроллер
# Модуль для импорта(ввода данных)
# Модуль для экспорта(вывод данных)
# Строка содержит id,имя,фамилию,номер телефона, комментрий - символ разделитель на 
# выбор(можно использовать пробел или запятые) + файл с хранением этих строк
# *Добавить сортировку по имени или по id
# *Добавить вывод только имени и фамилии

import view
import modul_work

def process():
    # print("controller = ",view.input_data())
    # print("sss", temp)
    while True:
        temp = view.input_data()
        if temp == 1:
            view.function_1()
        if temp == 2:
            view.function_2()
        if temp == 3:
            modul_work.function_3()
        if temp == 4:
            modul_work.function_4()            
        elif temp == 5:
            print("работа закончена")
            break

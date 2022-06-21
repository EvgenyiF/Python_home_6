from typing import List


def get_data():
    global a
    surname = input('Фамилия: ')
    name = input('Имя: ')
    number = input('Номер телефона: ')
    description = input('Описание: ')
    a = [surname,name,number,description]
    return a
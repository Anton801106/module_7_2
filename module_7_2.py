# Домашнее задание по теме "Позиционирование в файле".
# Задача "Записать и запомнить"

import io

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]


def custom_write(file_name, strings):
    strings_positions = {}
    file_name = 'test.txt'
    with io.open(file_name, 'w', encoding='utf-8') as file:
        for i in strings:
            position = file.tell()
            file.write(i + '\n')
            strings_positions[(len(strings_positions) + 1, position)] = i
        return strings_positions


result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

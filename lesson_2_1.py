import argparse

print('2.1.2 Задание 1', '\n**********')
print('Перейти в терминал, выполнить команду python')
print('1. print("Hello, World!"): Hello, World!')
print('2. Запустите печать в цикле, что бы вывести сообщение 10 раз:\n print("Hello, World!"):', ('Hello, '
                                                                                                  'World! '*10),
      '\n**********')

print('2.1.2 Задание 2, пункт 2', '\n**********')
print('Сделать доступной передачу аргументов при запуске файла: python3 lesson_02_01.py --name=Petr`')
print('1. Импортировать модуль argparse (предназначен для работы с аргументами командной строки):\nimport argparse')

parser = argparse.ArgumentParser(description="idPowers 2.1.2.2")
print('2. Создать объект ArgumentParser:\nparser = argparse.ArgumentParser(description="idPowers 2.1.2.2")\n')

parser.add_argument("--name", default='User', type=str, help="Enter a name")
print('Добавить аргумент --name:\nparser.add_argument("--name", default="User", type=str, help="Enter a name")\n')

args = parser.parse_args()
print('Парсим аргументы методом parse_args(), создав переменную args:\nargs = parser.parse_args()\n')

print(f'print(f"Hello, World! I am {args.name}"!):\n# если --name передан не будет, по дефолту будет стоять User')
print(f'Пишем в терминале:\npython "название_файла".py --name={args.name}')
print(f'Вывод: Hello, World! I am {args.name}!\n**********')

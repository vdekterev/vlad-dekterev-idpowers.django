print('2.4.1. Задание 2', '\n**********')

with open('new_file.txt', 'r+', encoding='utf-8') as file:
    file.write('Hello, world, how is it going?')
    file.seek(0)
    lst = [n for n in file.readline().split()]
print("1. Создаем файл new_file.txt\nwith open('new_file.txt', 'r+', encoding='utf-8') as file:\n    file.write('Hello, world, how is it going?')\n"
      "    file.seek(0)\n    lst = [n for n in file.readline().split()]")

with open('empty_file.txt', 'w', encoding='utf-8') as file:
    for el in lst:
        file.write(el + '\n\n')
print("2. Создаем пустой файл empty_file.txt:\nwith open('empty_file.txt', 'w', encoding='utf-8') as file:\n    for el in lst:\n        file.write(el + '\\n\\n')")
print('Результат:\nHello,\n\nworld,\n\nhow\n\nis\n\nit\n\ngoing?')
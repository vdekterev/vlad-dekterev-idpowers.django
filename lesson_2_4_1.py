print('2.4.1. Задание 1', '\n**********')

with open('cp1251-ru.txt', 'w', encoding='cp1251') as file:
    file.write('Привет, мир!')
print("1. Создан файл cp1251-ru.txt с кодировкой cp1251:\nwith open('cp1251-ru.txt', 'w', encoding='cp1251') as file:\n   file.write('Привет, Мир!')")
with open('utf-8-ru.txt', 'w', encoding='utf-8') as file:
    file.write('Привет, мир!')
print("Аналогично создан utf-8.txt с кодировкой utf-8:\nwith open('utf-8-ru.txt', 'w', encoding='utf-8') as file:\n   file.write('Привет, Мир!')\n")

with open('cp1251-en.txt', 'w', encoding='cp1251') as file:
    file.write('Hello, World!')
print("2. Создан файл cp1251-en.txt с кодировкой cp1251:\nwith open('cp1251-en.txt', 'w', encoding='cp1251') as file:\n   file.write('Hello, World!')")
with open('utf-8-en.txt', 'w', encoding='utf-8') as file:
    file.write('Hello, World!')
print("Аналогично создан utf-8-en.txt с кодировкой utf-8:\nwith open('utf-8-en.txt', 'w', encoding='utf-8') as file:\n   file.write('Hello, World!')")
print('\nВ обоих случаях, файл с кодировкой utf-8 занимает больше памяти, так как она, в отличии от cp1251, многобайтовая.\n')

print("3. Открыт файл cp1251-en.txt с кодировкой cp1251, указав при открытии кодировку utf-8:\nwith open('cp1251-en.txt', 'r', encoding='utf-8') as file:\n   f = file.read()\n   print(f)")
with open('cp1251-en.txt', 'r', encoding='utf-8') as file:
    f = file.read()
    print(f'Вывод: {f}')

print('В данном случае, файл открылся, ошибок не возникло.')


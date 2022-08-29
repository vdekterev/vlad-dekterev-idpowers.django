print('2.6.1 Задание 2', '\n**********')

print('1. Создаем строку из букв русского алфавита:\nletters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"\n')
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

print('2. Создаем вложенный список, состоящий из кортежей по типу: ("А", "а")\npairs = [(l.upper(), l) for l in letters]\n')
pairs = [(l.upper(), l) for l in letters]

print('3. Запускаем цикл:\nfor i in range(int(len(letters) / 3)):\n    print("^"*27)')
print("    print('| ', *pairs[i], ' || ', *pairs[i + 11], ' || ', *pairs[i + 22], ' |')")
print('print("^"*27)\n\nИтог:')

for i in range(int(len(letters) / 3)):
    print('^'*27)
    print('| ', *pairs[i], ' || ', *pairs[i + 11], ' || ', *pairs[i + 22], ' |')
print('^'* 27)


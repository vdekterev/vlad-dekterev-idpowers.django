print('2.6.1 Задание 1', '\n**********')
items = [2, 4, 5, 8, 9, 13]
print('Имеется список:\nitems = [2, 4, 5, 8, 9, 13]\nА также пустой список:\nnew_items = []')
new_items = []

print('Способ решения с помощью цикла while:\n')

while len(items) != 0:
    p = items.pop(items.index(items[0]))
    new_items.append(p * p)

print('while len(items) != 0:\n     p = items.pop(items.index(items[0]))\n     new_items.append(p * p)\n')
print(f'print("new_items")\nРезультат: {new_items}')

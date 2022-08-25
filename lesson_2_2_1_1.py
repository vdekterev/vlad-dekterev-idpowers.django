print('2.2.1 Задание 1', '\n**********')
actors = {}
print('1. Создан словарь: actors\nКод: actors = {}')
print(f'Словарь: {actors}', end='\n\n')

actors['amount'] = 10
print('2. Добавлен новый элемент с ключом типа str и значением типа int\nКод: actors["amount"] = 10')
print(f'Словарь: {actors}', end='\n\n')

actors[('John Travolta_age', 'Christoph Waltz_age')] = [68, 65]
print('3. Добавлен новый элемент с ключом типа кортеж(tuple) и значением типа список(list)\nКод: actors[("John Travolta_age", "Christoph Waltz_age")] = [68, 65]')
print(f'Словарь: {actors}', end='\n\n')

print('4. Получен элемент по ключу:', actors['amount'], '\nКод: actors["amount"]')
print(f'Словарь: {actors}', end='\n\n')

del actors['amount']
print('5. Удален элемент по ключу\nКод: del actors["amount"]')
print(f'Словарь: {actors}', end='\n\n')

print('6. Список ключей:', actors.keys(), '\nКод: del actors["amount"]')
print(f'Словарь: {actors}', end='\n\n')

print('7. Список значений', actors.values())
print(f'Словарь: {actors}', end='\n\n')
print('-------------')
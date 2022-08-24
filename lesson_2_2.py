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
print('-------------\n')

print('2.2.1 Задание 2', '\n**********')
names = {'Max', 'Eugene', 'Quentin', 'Ahmed', 'Max'}
print("1.Создано множество: names\nКод: names = {'Max', 'Eugene', 'Quentin', 'Ahmed', 'Max'}")
print(f'Множество: {names}', end='\n\n')
names.add('Vadim')
print('2. Добавлено новое значение: Vadim\nКод: names.add("Vadim")')
print(f'Множество: {names}', end='\n\n')

names.add('Quentin')
print('3. Добавлено, уже имеющееся в множестве: Quentin\nКод: names.add("Quentin")')
print(f'Множество: {names}', end='\n\n')

names.remove('Ahmed')
print('4. Удалено значение: Ahmed\nКод: names.remove("Ahmed")')
print(f'Множество: {names}', end='\n\n')

names.discard('Vladislav')
print('5. Удалено несуществующее значение без вызова ошибки\nКод: names.discard("Vladislav")')
print(f'Множество: {names}', end='\n\n')

names.add(('Kirill', 'George'))
print('6. Добавлен кортеж\nКод: names.add(("Kirill", "George"))')
print(f'Множество: {names}', end='\n\n')

names.update(['Michael', 'Valerie'])
print('Добавлен список\nКод: names.update(["Michael", "Valerie"])')
print(f'Множество: {names}', end='\n\n')

print('-------------')
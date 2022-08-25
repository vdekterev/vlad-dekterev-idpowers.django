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
print(f'Множество: {names}', end='\n')

print('-------------')
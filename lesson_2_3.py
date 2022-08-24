import random
print('2.3.2 Задание 1', '\n**********')

print("1. Создан список goods\nКод: goods = ['MacBook Air', 'Apple Watch', 'Airpods']")
goods = ['MacBook Air', 'Apple Watch', 'Airpods']
print(f'Список: {goods}\n')

print('2. Получен индекс произвольного элемента')
print('Рандомный элемент списка:',goods[random.randint(0, len(goods)-1)], '\nКод: goods[random.randint(0, ''len(goods)-1)]')

print('\n3. Добавлен элемент в конец списка\nКод: goods.append("iphone 13")')
goods.append('iphone 13')
print(f'Список: {goods}\n')

print("4. Добавлен элемент в середину списка:\nКод: goods.insert(len(goods)//2, 'iMac')")
goods.insert(len(goods)//2, 'iMac')
print(f'Список: {goods}\n')

print('5. Получен и удален последний элемент списка методом pop:\nКод: print(goods.pop(-1))')
print(f'Последний элемент списка: {goods.pop(-1)}')
print(f'Список: {goods}\n')

print("6. Создаем второй список:\nКод: new_goods = ['Sony Playstation 5', 'Xbox One', 'Nintendo Switch']")
new_goods = ['Sony Playstation 5', 'Xbox One', 'Nintendo Switch']
print('Дополняем первый список вторым методом extend:\ngoods.extend(new_goods)')
goods.extend(new_goods)
print(f'Список: {goods}\n')

print('7. Меняем сортировку списка:\nКод: goods.sort()')
goods.sort()
print(f'Список: {goods}\n')
goods.sort(reverse=True)
print('7. В обратную сторону:\nКод: goods.sort(reverse=True)')
print(f'Список: {goods}\n')

print('Второй способ:\nКод: print(sorted(goods))')
print(f'Вывод: {sorted(goods)}\n')
print('И в обратную сторону:\nКод: print(sorted(goods)[::-1])')
print(f'Вывод: {sorted(goods)[::-1]}')
print('----------\n')

print('2.3.2 Задание 2', '\n**********')
non_existing_keys = {'Xiaomi', 'Samsung', 'Phillips', 'Polaris', 'Scarlett'}

prices = {'iPhone 11': 48900, 'MacBook Pro 2017': 63000}
print("1. Создан словарь prices\nКод: prices = {'iPhone 11': 48900, 'MacBook Pro 2017': 63000}\n"
      "А также словарь с несуществующими ключами:\nnon_existing_keys = {'Xiaomi', 'Samsung', 'Phillips', 'Polaris', "
      "'Scarlett'}")
print(f'Словарь: {prices}\n')

print('2. Попробуем получить несуществующий ключ\nprices["Airpods"]\n#Обойдем ошибку с помощью обработки '
      'исключений\ntry:\n    prices[non_existing_keys.pop()]\nexcept Exception as ex:\n    print(f"Нет такого ключа: {ex}")')
try:
    prices[non_existing_keys.pop()]
except Exception as ex:
    print(f'Нет такого ключа: {ex}')
print(f'Словарь: {prices}\n')

print('3. Получаем несуществующий ключ методом get()\nКод: prices.get(non_existing_keys.pop())')
print('Результат:', prices.get(non_existing_keys.pop(), 0))
print(f'Словарь: {prices}\n')

print("4. Обновляем словарь несколькими ключами\nСоздаем новый словарь: new_prices={'Airpods': 9000, 'iMac': 120000, "
      "'Apple Watch Series 7': 35900}\n")
new_prices = {'Airpods': 9000, 'iMac': 120000, 'Apple Watch Series 7': 35900, 'iPhone 11': 39000}
print('5. Объединяем словари + создаем из них новый:\nprices.update(new_prices)\nfinal_prices = prices')
prices.update(new_prices)
final_prices = prices
print(f'Словарь: {final_prices}\n')
print('6. Если ключи словарей пересекаются, ключом становится более поздний:')
f = {'одинаковый ключ': 'старый ключ', '2': 2}
s = {'одинаковый ключ': 'новый ключ', '4': 4}
f.update(s)
res = f
print("f = {'одинаковый ключ': 'старый ключ', '2': 2}")
print("s = {'одинаковый ключ': 'Новый ключ', '4': 4}\nf = f.update(s)\nres = f")
print(f'Вывод: {res}\n')

print('2.3.2 Задание 3', '\n**********')
print("1. Создаем два множества с частично одинаковыми значениями:\nnames_one = {'Max', 'Eugene', 'Quentin', 'Ahmed', 'Max'}\nnames_two = {'Yuri', 'Dima', 'Kirill', 'Kirill', 'Anton', 'Yuri'}")

names_one = {'Max', 'Eugene', 'Quentin', 'Ahmed', 'Max', 'Dima', 'Yuri'}
names_two = {'Yuri', 'Dima', 'Kirill', 'Kirill', 'Anton', 'Yuri'}
print(f'Множество 1: {names_one}\nМножество 2: {names_two}\n')

print('2. Объединяем созданные множества:\nunion = names_one.union(names_two) или union = names_one | names_two')
union = names_one | names_two
print(f'Объединенное множество: {union}\n')

print('3. Выполняем пересечение множеств:\ncross = names_one.insertion(names_two) или cross = names_one & names_two')
cross = names_one & names_two
print(f'Пересеченные множества: {cross}\n')


print('4. Выполняем операцию разности множеств:\ndifference = names_one.difference(names_two) или difference = '
      'names_one - names_two')
difference = names_one - names_two
print(f'Разность: {difference}\n')

print('5. Выполняем операцию симметричной разности множеств:\nsym_difference = names_one.symmetric_difference(names_two) или sym_difference = names_one ^ names_two')
sim_difference = names_one ^ names_two
print(f'Симметричная разность: {sim_difference}\n')

print('Разница между вышеперечесленными разностями\nРазность: объекты, которые есть в первом, но не во втором '
      'множестве.')
print('Симметричная разность: все объекты, кроме тех, что есть в обоих множествах.\n')
print('6. Операции с символами уже выполнены в пунктах выше\n"+" - такой оператор не работает с множествами\n'
      '"-" - разность множеств\n"|" - объединение множеств\n"^" - симметричная разность множеств\n'
      '"&" - пересечение множеств')

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
print(f'Вывод: {res}')
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
print('----------')
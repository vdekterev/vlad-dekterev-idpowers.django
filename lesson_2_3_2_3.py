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
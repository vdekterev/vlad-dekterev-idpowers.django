import random
print('2.7.3 Задание 3', '\n**********')
print('Напишите функцию sum_range(start, end), '
      'которая суммирует все целые числа от значения start до величины end включительно.\n'
      'Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.\n')
print('import random    # импортируем модуль random\nОпределяем функцию:\n'
      'def sum_range(start, end):\n    if start > end:\n        '
      'start, end = end, start\n    return(sum(range(start, end + 1))\n')

print('Также это задание можно решить через рекурсию:\n'
      'def sum_range_recursion(start, end):\n    if start > end:\n        '
      'start, end = end, start\n    if end == start:\n        return end\n    else:\n    '
      'return end + sum_range_recursion(start, end - 1)\n\n'
      'Вызовем обе функции по 10 раз:\nfor _ in range(10):\n    a = random.randint(1, 100)\n'
      '    b = random.randint(1, 100)\n    print(f"a = {a}, b = {b}\\nsum_range({a}, {b}) = {sum_range(a, b)}\\n\n'
      '    f"sum_range_recursion({a}, {b}) = {sum_range_recursion(a, b)}"\n    print("----------")\n')

print('Вывод:')
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


def sum_range_recursion(start, end):
    if start > end:
        start, end = end, start
    if end == start:
        return end
    else:
        return end + sum_range_recursion(start, end - 1)


for _ in range(10):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(f'a = {a}, b = {b}\nsum_range({a}, {b}) = {sum_range(a, b)}\n'
          f'sum_range_recursion({a}, {b}) = {sum_range_recursion(a, b)}')
    print('----------')

print('2.7.3 Задание 1', '\n**********')
print('Передайте в функцию ниже аргументы всеми возможными способами:')
print('def print_sum(a, b):\n   print(a + b)')


def print_sum(a, b):
    print(a + b)


print('1. Передать позиционными аргументами:\nprint_sum(10, 20)')
print('Вывод:\n---')
print_sum(10, 20)
print('---')
print('2. Передать по ключевым словам:\nprint_sum(a=10, b=20)')
print('Вывод:\n---')
print_sum(a=10, b=20)
print('---')
print('3. Передать через *args списком или кортежем:\nlst = [10, 20]\nprint_sum(*lst[:2]) '
      '#используем срез во избежании ошибок')
lst = [10, 20]
print('Вывод:\n---')
print_sum(*lst[:2])
print('---')
print('4. Передать через **kwargs словарем:\nd = {"a": 10, "b": 20}\nprint_sum(**d)')
d = {"a": 10, "b": 20}
print('Вывод:\n---')
print_sum(**d)
print('---')
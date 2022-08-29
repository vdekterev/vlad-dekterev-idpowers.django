print('2.6.1 Задание 3', '\n**********')

print('1. Во избежание дублирования кода, создадим функцию, которая будет возвращать кортеж из делителей переданного числа:\n')
print('def get_divisors(number):\n    return tuple((n for n in range(1, number + 1) if number % n == 0))\n')


def get_divisors(number):
    return tuple((n for n in range(1, number + 1) if number % n == 0))


print('2. Попросим Анну ввести данные ей числа через пробел:\ntask_numbers = tuple(map(int, input().split()))')
task_numbers = tuple(map(int, input('Введите числа через пробел:\n').split()))

print('3. Запускаем цикл, который пройдет по всем введенным числам и вернет их делители:\n')

print("for n in task_numbers:\n    print(f'Делители числа {n}:', *get_divisors(n)):\n")

for n in task_numbers:
    print(f'Делители числа {n}:', *get_divisors(n))





# 23436 190187200 380457890232
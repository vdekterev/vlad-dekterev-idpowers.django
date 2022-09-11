print('2.7.3 Задание 2', '\n**********')
print('Создайте функцию three_args(), '
      'которая принимает 1, 2 или 3 строго ключевых параметра.\n'
      'В результате ее работы на печать в терминал выводятся значения '
      'переданных переменных,\nно только если они не равны None.\n'
      'Пример: Переданы аргументы: var1 = 2, var3 = 10.\n----------')
print('Создаем функцию:\ndef three_args(*, var1, var2, var3):\n    '
      'indx = 0\n    output = 0\n    for n in var1, var2, var3:\n    '
      '    indx += 1')
print('        output.append(f"var{indx} = {n}" if n else None)\n    '
      'while None in output:\n'
      '        output.remove(None)\n    if len(output) > 1:\n        '
      'print(f"Переданы аргументы: {', '.join(output)}")\n    '
      'elif len(output) == 1:\n        print(f"Передан аргумент: {output[0]}")\n    '
      'else:\n        print("Аргументы отсутствуют")\n----------')

print('Вызываем функцию:\nthree_args(var1=1, var2=None, var3= "wassup")')


def three_args(*, var1, var2, var3):
    indx = 0
    output = []
    for n in var1, var2, var3:
        indx += 1
        output.append(f'var{indx} = {n}' if n else None)
    while None in output:
        output.remove(None)
    if len(output) > 1:
        print(f'Переданы аргументы: {", ".join(output)}')
    elif len(output) == 1:
        print(f'Передан аргумент: {output[0]}')
    else:
        print('Аргументы отсутствуют')

print('Вывод:')
three_args(var1=1, var2=None, var3= "wassup")
print('----------')
print('Вызываем функцию с одним аргументом:\nthree_args(var1=None, var2=None, var3= "theonlyonevariable")')
print('Вывод:')
three_args(var1=None, var2=None, var3= "theonlyonevarg")
print('----------')
print('Вызываем функцию без аргументов:\nthree_args(var1=None, var2=None, var3= None)')
print('Вывод:')
three_args(var1=None, var2=None, var3= None)
print('----------')

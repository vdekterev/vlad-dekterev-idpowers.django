print('2.7.3 Задание 4', '\n**********')
print('Определяем функцию:\ndef pangramm_checker(s):\n    '
      'res = set(l for l in s.lower().strip() if l.isalpha())\n    '
      'return ("Это НЕ панграмма", "Это панграмма")[len(res) == 33]\n\n'
      'Вызываем функцию, выводим ее результат на печать:\n'
      'print(pangramm_checker("Эй, цирюльникъ, ёжик выстриги, да щетину ряхи сбрей, феном вошь за печь гони"))\n'
      'Вывод:')


def pangramm_checker(s):
    res = set(l for l in s.lower().strip() if l.isalpha())
    return ('Это НЕ панграмма', 'Это панграмма')[len(res) == 33]


print(pangramm_checker('Эй, цирюльникъ, ёжик выстриги, да щетину ряхи сбрей, феном вошь за печь гони'), '\n----------')
print('print(pangramm_checker("Быстрая коричневая лиса перепрыгивает через ленивую собаку))')
print('Вывод:')
print(pangramm_checker('Быстрая коричневая лиса перепрыгивает через ленивую собаку'), '\n----------')
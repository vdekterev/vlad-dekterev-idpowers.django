print('2.7.3 Задание 5', '\n**********')

print('Определяем функцию:\ndef pascal_triangle(N):\n   triangle = []\n   for i in range(N):\n'
      '      row = [1] * (i + 1)\n      for j in range(i + 1):\n         if j != 0 and j != 1:\n'
      '            row[j] = triangle[i-1][j-1] + triangle[i-1][j]\n         triangle.append(row)\n\n'
      '   for s in triangle:\n      print("   " * (N-len(s)), *s, "   " * (N-len(s)), sep="  |  "')

print('\nВызываем функцию:\npascal_triangle(5)\n\nВывод:')


def pascal_triangle(N):
    triangle = []
    for i in range(N):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
               row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    for s in triangle:
        print('   ' * (N-len(s)), *s, '   ' * (N-len(s)), sep='  |  ')


pascal_triangle(5)

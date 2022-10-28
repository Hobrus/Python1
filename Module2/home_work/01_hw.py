# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Формат входных данных
# Вводятся 3 натуральных числа n, m и k. Точно известно, что  k ≠ n ⋅ m.
# Формат выходных данных
# Выведите «YES», если можно отломить от шоколадки ровно k долек, и «NO» иначе.

chocolate_bar_size_by_x = int(input('Enter Chocolate Bar Size By \'X\': '))
chocolate_bar_size_by_y = int(input('Enter Chocolate Bar Size By \'Y\': '))
piece_of_chocolate_size = int(input('Enter Piece Of Chocolate Bar: '))

if piece_of_chocolate_size != chocolate_bar_size_by_x * chocolate_bar_size_by_y and (piece_of_chocolate_size == chocolate_bar_size_by_x or piece_of_chocolate_size == chocolate_bar_size_by_y):
    print('YES')
else:
    print('NO')

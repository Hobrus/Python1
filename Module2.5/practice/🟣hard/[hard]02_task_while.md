## "Диагонали символами"

### Задание

Даны сторона квадрата. Вывести его диагонали символами #

### Формат входных данных

Дано целое число n, длина стороны квадрата. 1 < n < 20 

### Формат выходных данных

Вывести диагонали квадрата символами # (см. примеры)

#### Примеры

n = 6 
```
#    #
 #  #
  ##
  ##
 #  #
#    #
```
n = 3
```
# #
 #
# #
```
### Решение задачи

n = int(input('n: '))

if n % 2 == 0:
    i = 1
    spaces_count_left = 0
    spaces_count_center = n - 2
    while i <=  n:
        if i == 1 or i == n:
            spaces_count_left = 0
            spaces_count_center = n - 2
        elif 1 < i < n / 2:
            spaces_count_left += 1
            spaces_count_center -= 2
        elif i == (n / 2) + 1 or i == n / 2:
            spaces_count_left = (n / 2) - 1
            spaces_count_center = 0
        elif n / 2 < i < n:
            spaces_count_left -= 1
            spaces_count_center += 2

        print ((' ' * int(spaces_count_left)) + '#' + (' ' * int(spaces_count_center)) + '#')

        i += 1


else:
    i = 1
    spaces_count_left = 0
    spaces_count_center = n - 2
    while i <=  n:
        if i == 1 or i == n:
            spaces_count_left = 0
            spaces_count_center = n - 2
        elif 1 < i <= n // 2:
            spaces_count_left += 1
            spaces_count_center -= 2
        elif i == (n // 2) + 1:
            spaces_count_left = n // 2
            spaces_count_center = -1
        elif (n // 2) <= i < n:
            spaces_count_left -= 1
            spaces_count_center += 2
        if i != (n // 2) + 1:
            print ((' ' * int(spaces_count_left)) + '#' + (' ' * int(spaces_count_center)) + '#')
        else:
            print((' ' * int(spaces_count_left)) + '#')
        i += 1
```

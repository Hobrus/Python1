## "Подсчет длинных слов"

### Задание

Даны две строки s1 и s2. Определите, можно ли составить строку s2, используя только символы из строки s1 (каждую букву можно использовать только один раз).

### Формат входных данных

Даны две строки.

### Формат выходных данных

Вывести "Да", если из символов строки s1 можно составить строку s2 и "Нет", если нельзя.

### Решение задачи

s1 = 'Мама мыла раму'
s1_low = s1.lower()
s1_set = set(s1_low)
s1_dict = {s: s1_low.count(s) for s in s1_set}

s2 = 'Мама'
s2_low = s2.lower()
s2_set = set(s2_low)
s2_dict = {s: s2_low.count(s) for s in s2_set}

#print(s1_dict)
#print(s2_dict)
no_count = 0

for letter, letter_count in s2_dict.items():
    if letter not in s1_dict.keys() or s1_dict[letter] < letter_count:
        no_count +=1

if no_count > 0:
    print('Нельзя')
else:
    print('Можно')
---


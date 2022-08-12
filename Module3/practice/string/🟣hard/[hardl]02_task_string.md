## "Подсчет длинных слов"

### Задание

Даны две строки s1 и s2. Определите, можно ли составить строку s2, используя только символы из строки s1 (каждую букву можно использовать только один раз).

### Формат входных данных

Даны две строки.

### Формат выходных данных

Вывести "Да", если из символов строки s1 можно составить строку s2 и "Нет", если нельзя.

### Решение задачи

```python
s1 = "если бы да кабы во рту выросли грибы?"
s2 = "ели вы да?"
s1_list = []
s2_list = []

for i in s1:
  s1_list.append(i)

for i in s2:
  s2_list.append(i)

s1_list_unique = [*(set(s1))]

s2_make_from_s1_unique = []
for i in s2_list:
  if i in s1_list_unique and i != ' ':
    s2_make_from_s1_unique.append(i)
    s1_list_unique.remove(i)

s2_list_wo_space = []
for i in s2_list:
  if i != ' ':
    s2_list_wo_space.append(i)

if  s2_make_from_s1_unique == s2_list_wo_space:
  print('может')
else:
  print('нет')
```

---


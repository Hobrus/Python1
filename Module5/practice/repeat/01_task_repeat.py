# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, of, to):
    pass

import random
lst = []
def gen_list(of, to, size):
    for i in range(size):
        lst.append(random.randint(of, to))
    return lst

a = 0
b = 15
c = 5
result = gen_list(a,b,c)
print(result)

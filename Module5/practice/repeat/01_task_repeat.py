import random


def gen_list(size, of, to):
    lst = []
    for i in range(size):
        lst.append(random.randint(of, to))
    return lst
print(gen_list(3, 9, 10))

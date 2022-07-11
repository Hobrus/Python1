# Является ли палиндромом?
# Напишите функцию, проверяющую является ли число палиндромом.
# палиндром - число одинаково читающееся слева направо, так и справа налево.
#  Пример палиндрома: 12321

def palindrome(number):
    pass

def palindrom(number):
    number = str(number)
    if number[::2] == number[::-2]:
        print('число является палиндромом')
    else:
        print('число не является палиндромом')
number = int(input('введите число '))
print(palindrom(number))

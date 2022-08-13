# Дана строка состоящая из слов, все слова разделены ровно одним пробелом. Знаки препинания отсутствуют.
# Найдите первое слово, начинающееся на букву "б"
# если слова на эту букву нет, выведите "слов на б нет"

text = input('text: ')

if text[0] == 'б':
    end = text.find(' ')
    if end >= 0:
        print(text[:end])
    else:
        print(text)
else:
    find_start = text.find(' б')
    start = find_start + 1
    if find_start >= 0:
        end = text.find(' ', start)
        if end >= 0:
            print(text[start:end])
        else:
            print(text[start:])
    else:
        print('No words with "б"')

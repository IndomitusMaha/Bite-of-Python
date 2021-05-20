"""

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

def clense(string):
    global something
    string = string.lower()
    for i in string:
        for j in forbidden:
            if i == j:
                string = string.replace(i, '')
                something = string
                print(something)


something = input('Введите текст: ')
print(something)
forbidden = ('!', '?', '.', '…', '!', ':', ';', '-', '—', '( )', '[ ]', '’', '“', '”', '/', ' ')
clense(something)

while True:
    if (is_palindrome(something)):
        print("Да, это палиндром")
        something = input('Введите текст: ')
        clense(something)
    elif something == "Stop":
        break
    else:
        print("Нет, это не палиндром")
        something = input('Введите текст: ')
        clense(something)
"""
poem = '''\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
используй Python!
'''
"""
f = open('poem.txt', 'w') # открываем для записи (writing)
f.write(poem) # записываем текст в файл
f.close() # закрываем файл

f = open('poem.txt') # если не указан режим, по умолчанию подразумевается
# режим чтения ('r'eading)
while True:
    line = f.readline()
    if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
        break
    print(line, end='')
f.close() # закрываем файл
"""

import pickle
# имя файла, в котором мы сохраним объект
shoplistfile = 'shoplist.data' #novii yip faila
# список покупок
shoplist = ['яблоки', 'манго', 'морковь']
# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещаем объект в файл
f.close()
del shoplist # уничтожаем переменную shoplist
# Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загружаем объект из файла
print(storedlist)
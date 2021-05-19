"""
# Это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
print('Я должен сделать ', len(shoplist), 'покупок.')
print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')
print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)
print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)
print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)
"""

"""
# kortezh (tuple)
zoo = ('питон', 'слон', 'пингвин') # помните, что скобки не обязательны
print('Количество животных в зоопарке -', len(zoo))
new_zoo = 'обезьяна', 'верблюд', zoo
print('Количество клеток в зоопарке -', len(new_zoo))
print('Все животные в новом зоопарке:', new_zoo)
print('Животные, привезённые из старого зоопарка:', new_zoo[2])
print('Последнее животное, привезённое из старого зоопарка -', new_zoo[2][2])
print('Количество животных в новом зоопарке -', len(new_zoo)-1+len(new_zoo[2]))

"""
"""
#library
ab = { 'Swaroop' : 'swaroop@swaroopch.com',
'Larry' : 'larry@wall.org',
'Matsumoto' : 'matz@ruby-lang.org',
'Spammer' : 'spammer@hotmail.com'
}
print("Адрес Swaroop'а:", ab['Swaroop'])
# Удаление пары ключ-значение

del ab['Spammer']
print('\nВ адресной книге {0} контактов\n'.format(len(ab)))
for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])
    
"""
"""
# peremennye eto vsego lish ssilki
print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist # mylist - лишь ещё одно имя, указывающее на тот же объект!
del shoplist[0] # Я сделал первую покупку, поэтому удаляю её из списка
print('shoplist:', shoplist)
print('mylist:', mylist)
# Обратите внимание, что и shoplist, и mylist выводят один и тот же список
# без пункта "яблоко", подтверждая тем самым, что они указывают на один объект.
print('КОПИРАВАНИЕ С ПОМОЩЬЮ ПОЛНОЙ ВЫРЕЗКИ')
mylist = shoplist[:] # создаём копию путём полной вырезки
del mylist[0] # удаляем первый элемент
print('shoplist:', shoplist)
print('mylist:', mylist)

#"""

"""
name = 'Swaroop' # Это объект строки
if name.startswith('Swa'):
    print('Да, строка начинается на "Swa"')
if 'a' in name:
    print('Да, она содержит строку "a"')
if name.find('war') != -1:
    print('Да, она содержит строку "war"')

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))
"""
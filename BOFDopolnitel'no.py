"""def twosum(a, b):
    c = a + b
    return c

print(twosum(3,4))"""

"""
# peredacha kortezhei
def get_error_details():
    return (2, 'описание ошибки No2')

errnum, errstr = get_error_details()
print(errnum)
print(errstr)

a, *b = [1, 2, 3, 4]
print(a)
print(b)
print("----------")
# invertacia kortezhei
a, b = b, a
print(a)
print(b)"""

"""
# bloki v odno virazheniye
flag = True
if flag: print('Да') """

"""
points = [ { 'x' : 2, 'y' : 3 }, { 'x' : 4, 'y' : 1 } ]
points.sort(key=lambda i : i['y'])
print(points)"""

"""
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)"""

"""
def powersum(power, *args):
    '''Возвращает сумму аргументов, возведённых в указанную степень.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

t = powersum(2, 4, 5)
print(t)"""

"""
#fuckcii dlya vipolnenie komand v stokah
exec('print("Здравствуй, Мир!")')
eval('2*3') """

"""
# assert существует для того, чтобы указать, что нечто является истиной.
mylist = ['item']
assert len(mylist) >= 1
mylist.pop()
'item'
mylist
[]
assert len(mylist) >= 1 """

"""
# repr используется для получения канонического строкового представления
# объеta
i = []
i.append('item')
print(repr(i))
print(eval(repr(i)))
print(eval(repr(i)) == i) """

# eta stroka ne mozhet' bit' obrabotana iz za "r"
R = r'Перевод строки обозначается \n   '
print(R.lower)
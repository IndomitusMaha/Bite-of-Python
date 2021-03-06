class Person1:
    pass # Пустой блок
p = Person1()
print(p)
print("88888")

class Person2:
    def sayHi(self):
        print('Привет! Как дела?')
p = Person2()
p.sayHi()
print("88888")

class Person3:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Привет! Меня зовут', self.name)

p = Person3('Swaroop')
p.sayHi()

Person3('Swaroop').sayHi()
print("88888")

class Robot:
    '''Представляет робота с именем.'''
    # Переменная класса, содержащая количество роботов
    population = 0
    def __init__(self, name):
        '''Инициализация данных.'''
        self.name = name
        print('(Инициализация {0})'.format(self.name))
    # При создании этой личности, робот добавляется
    # к переменной 'population'
        Robot.population += 1
    def __del__(self):
        '''Я умираю.'''
        print('{0} уничтожается!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))
    def sayHi(self):
        '''Приветствие робота.
        Да, они это могут.'''
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
    def howMany():
        '''Выводит численность роботов.'''
        print('У нас {0:d} роботов.'.format(Robot.population))
    howMany = staticmethod(howMany)

droid1 = Robot("Titan")
droid1.sayHi()
Robot.howMany()
droid2 = Robot("Knight")
Robot.howMany()
IHNINnedi = Robot("Gundum")
Robot.howMany()
print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")

del droid1
del droid2

print("8888888888")

class SchoolMember:
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print() # печатает пустую строку
members = [t, s]

for member in members:
    member.tell() # работает как для преподавателя, так и для студента
print("8888888888888888888")

#!/usr/bin/env python
# Filename: inherit_abc.py
from abc import *

class SchoolMember(metaclass=ABCMeta):
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    @abstractmethod
    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''Представляет преподавателя.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))
        def tell(self):
            SchoolMember.tell(self)
            print('Зарплата: "{0:d}"'.format(self.salary))
class Student(SchoolMember):
    '''Представляет студента.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

#t = Teacher('Mrs. Shrividya', 40, 30000)
#s = Student('Swaroop', 25, 75)
#m = SchoolMember('abc', 10)
# Это приведёт к ошибке: "TypeError: Can't instantiate abstract class
# SchoolMember with abstract methods tell"

print() # печатает пустую строку
#members = [t, s]
#for member in members:
#    member.tell() # работает как для преподавателя, так и для студента
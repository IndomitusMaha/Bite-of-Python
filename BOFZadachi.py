Telefonnaya_kniga = {
    'Mukagali' : "+77012088044",
    'Rinad' : "+77025516646",
    'Kanat' : "+77752601300"}

def book():
    for i in Telefonnaya_kniga:
        print(i+" "+Telefonnaya_kniga[i])


def naiti(chel):
    for i in Telefonnaya_kniga:
        if chel == i:
            print(i+' '+Telefonnaya_kniga[i])

def add():
    print(" You want to addd person in a book")
    name = input("Name: ")
    number = input("Number: ")
    pass

def dellete(chel):
    for i in Telefonnaya_kniga:
        if chel == i:
            a = i
    del Telefonnaya_kniga[a]
    book()

print("Avalible commands:\n Book\n Find\n Dellete")
action = input("What do you want to do? ")

if action == 'Book':
    book()
elif action == 'Find':
    person = input('Who do you want to find? ')
    naiti(person)
elif action == 'Dellete':
    person = input('Who do you want to dellate? ')
    dellete(person)
else:
    print("There is no such command")

"""
class Kontact():
    def __init__(self, name, number):
        "Initializing Kontacts"
        self.n = name
        self.num = number

    def naiti(chel):
        for i in Kontact:
            if chel == i:
                print(self.n + ' ' + self.num)

    def book(self):
        pass

    def add(self):
        pass

Names = [Mukagali, Rinad, ]

print("Avalible commands:\n Book\n Find\n Add")
action = input("What do you want to do? ")

if action == 'Book':
    Kontact.book()
elif action == 'Find':
    person = input('Who do you want to find? ')
    Kontact.naiti(person)
elif action == 'Add':
    Kontact.add()
    pass
else:
    print("There is no such command")"""


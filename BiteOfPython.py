"""
# nonlocal
def func_outer():
    x = 2
    print('x равно', x)
    def func_inner():
        nonlocal x
        x = 5
        print("Во внутренней ф-ий", x)
    func_inner()
    print('Локальное x сменилось на', x)
func_outer() """

"""
# argumenty po umolchaniu
def say(message, times = 1):
    print(message * times)

say('Привет')
say('Мир', 5) """

"""
# kluchevii argumenti
def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100) """


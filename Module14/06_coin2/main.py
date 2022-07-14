# TODO здесь писать код

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
radius = float(input('Введите радиус: '))


def findCoin (x, y):
    if (-radius <= x <= radius) and (-radius <= y <= radius):
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


findCoin(x, y)

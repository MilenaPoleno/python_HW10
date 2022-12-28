"""Создать не менее двух дескрипторов
для атрибутов классов, которые вы
создали ранее в ДЗ"""


class NonNegative:

    def __init__(self, my_cell):
        self.my_cell = my_cell

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_cell]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_cell] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_cell]


class Cell:
    quantity = NonNegative('quantity')
    other = NonNegative('other')

    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * "0"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if (self.quantity - other.quantity) > 0:
            return Cell(self.quantity - other.quantity)
        else:
            return "Клеток не может быть меньше нуля!"

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity / other.quantity))


print("0 - обозначение клетки")
user_1 = Cell(5)
user_2 = Cell(10)

print(user_1)
print(user_2)
print(user_1 + user_2)
print(user_1 - user_2)
print(user_2 - user_1)
print(user_1 * user_2)
print(user_2 / user_1)

user_3 = Cell(-5)



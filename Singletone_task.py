"""Создать метакласс для паттерна
Синглтон (см. конец вебинара)"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


class MyMeta(metaclass=Singleton):
    pass


class UserClass():
    pass


x = MyMeta()
y = MyMeta()
print(x == y)

m = UserClass()
n = UserClass()
print(m == n)


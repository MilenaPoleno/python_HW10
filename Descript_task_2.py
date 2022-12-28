class TypedProperty:
    def __init__(self, name, type_name, default=None):
        self.name = "_" + name
        self.type = type_name
        self.default = default if default else type_name()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Значение должно быть типа %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("Невозможно удалить атрибут")


class Road:

    _lengh = TypedProperty("_lengh", int)
    _width = TypedProperty("_width", int)
    weight = TypedProperty("weight", int)
    depth = TypedProperty("depth", int)

    def __init__(self, _length, _width, weight, depth):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.depth = depth

    def mass(self):
        l = self._length
        wi = self._width
        we = self.weight
        d = self.depth
        result = l * wi * we * d / 1000
        return result

r = Road(20, 5000, 'lol', 5)
print(f"Понадобится масса {r.mass()} тонн")


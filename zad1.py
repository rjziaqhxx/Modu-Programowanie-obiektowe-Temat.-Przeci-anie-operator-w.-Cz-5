class Circle:
    def __init__(self, ray, lenght):
        self.ray = ray
        self.lenght = lenght

    def __str__(self):
        return f'Ray - {self.ray}, Lenght - {self.lenght}'

    def __eq__(self, other):
        return self.ray == other.ray
    
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.lenght < other.lenght
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.lenght > other.lenght
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, Circle):
            return self.lenght <= other.lenght
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.lenght >= other.lenght
        return NotImplemented
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.ray + other.ray, self.lenght + other.lenght)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Circle):
            return Circle(self.ray - other.ray, self.lenght - other.lenght)
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, Circle):
            self.ray += other.ray
            return self
        return NotImplemented
    
    def __isub__(self, other):
        if isinstance(other, Circle):
            self.ray -= other.ray
            return self
        return NotImplemented
    
obj1 = Circle(5, 10)
obj2 = Circle(6, 15)

print(obj1 == obj2, obj1 > obj2, obj1 < obj2, obj1 >= obj2, obj1 <= obj2)
obj3 = obj1 + obj2
print(obj3)
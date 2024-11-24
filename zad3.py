class Airplane:
    def __init__(self, airplane_type, max_passengers):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers

    def __str__(self):
        return f"airplane Type - {self.airplane_type}, max passengers - {self.max_passengers}"

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.airplane_type == other.airplane_type
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, int):
            return Airplane(self.airplane_type, self.max_passengers + other.max_passengers)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, int):
            return Airplane(self.airplane_type, self.max_passengers - other.max_passengers)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.max_passengers += other.max_passengers
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, int):
            self.max_passengers -= other.max_passengers
            return self
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

airplane1 = Airplane("Boeing", 180)
airplane2 = Airplane("Airbus", 150)

print(airplane1 == airplane2)
print(airplane1 + 20)
print(airplane2 - 10)
airplane1 += 30
print(airplane1)
airplane2 -= 5
print(airplane2)
print(airplane1 > airplane2)
print(airplane1 <= airplane2)
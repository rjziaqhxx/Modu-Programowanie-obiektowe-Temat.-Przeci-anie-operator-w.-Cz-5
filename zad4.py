class Apartment:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __str__(self):
        return f"area - {self.area}, price - {self.price}"

    def __eq__(self, other):
        if isinstance(other, Apartment):
            return self.area == other.area
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Apartment):
            return self.area != other.area
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Apartment):
            return self.price > other.price
        return NotImplemented

apartment1 = Apartment(50, 100000)
apartment2 = Apartment(60, 120000)
apartment3 = Apartment(50, 110000)

print(apartment1 == apartment3)
print(apartment1 != apartment2)
print(apartment1 > apartment2)
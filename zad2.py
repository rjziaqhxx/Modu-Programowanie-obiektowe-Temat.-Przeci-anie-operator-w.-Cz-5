class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag >= 0 else f"{self.real} - {-self.imag}i"

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real = self.real * other.real - self.imag * other.imag
            imag = self.real * other.imag + self.imag * other.real
            return Complex(real, imag)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Complex):
            denom = other.real**2 + other.imag**2
            if denom == 0:
                raise ValueError("Cannot divide by zero.")
            real = (self.real * other.real + self.imag * other.imag) / denom
            imag = (self.imag * other.real - self.real * other.imag) / denom
            return Complex(real, imag)
        return NotImplemented

z1 = Complex(3, 2)
z2 = Complex(1, -4)

z3 = z1 + z2
print(f"Z1 + Z2 = {z3}")

z4 = z1 - z2
print(f"Z1 - Z2 = {z4}")

z5 = z1 * z2
print(f"Z1 * Z2 = {z5}")

z6 = z1 / z2
print(f"Z1 / Z2 = {z6}")
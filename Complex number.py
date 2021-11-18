class ComplexNumber:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def show(self):
        if self.imaginary < 0:
            print(f"{self.real} - {-self.imaginary}i")
        else:
            print(f"{self.real} + {self.imaginary}i")

    def sum(self, other):
        result = ComplexNumber()
        result.real = self.real + other.real
        result.imaginary = self.imaginary + other.imaginary
        return result

    def sub(self, other):
        result = ComplexNumber()
        result.real = self.real - other.real
        result.imaginary = self.imaginary - other.imaginary
        return result

    def mul(self, other):
        result = ComplexNumber()
        result.real = self.real * other.real + self.imaginary * -other.imaginary
        result.imaginary = self.real * other.imaginary + self.imaginary * other.real
        return result


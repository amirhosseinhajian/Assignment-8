class Fraction:
    def __init__(self, s=0, m=None):
        self.soorat = s
        self.makhraj = m

    def show(self):
        print(self.soorat, "/", self.makhraj)

    def mul(self, other):
        result = Fraction()
        result.soorat = self.soorat * other.soorat
        result.makhraj = self.makhraj * other.makhraj
        result.simplify()
        return result


    def sum(self, other):
        result = Fraction()
        result.soorat = self.soorat * other.makhraj + self.makhraj * other.soorat
        result.makhraj = self.makhraj * other.makhraj
        result.simplify()
        return result

    def sub(self, other):
        result = Fraction()
        result.soorat = self.soorat * other.makhraj - self.makhraj * other.soorat
        result.makhraj = self.makhraj * other.makhraj
        result.simplify()
        return result

    def div(self, other):
        result = Fraction()
        result.soorat = self.soorat * other.makhraj
        result.makhraj = self.makhraj * other.soorat
        result.simplify()
        return result

    def simplify(self):
        if self.soorat >= self.makhraj:
            base = self.soorat / 2
        else:
            base = self.makhraj / 2
        for i in range(int(base), 1, -1):
            if self.soorat % i == 0 and self.makhraj % i == 0:
                self.soorat = int(self.soorat / i)
                self.makhraj = int(self.makhraj / i)


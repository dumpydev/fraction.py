class fraction:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def subtract(self, other):
        return fraction(self.a * other.b - self.b * other.a, self.b * other.b)
    def add(self, other):
        return fraction(self.a * other.b + self.b * other.a, self.b * other.b)
    def multiply(self, other):
        return fraction(self.a * other.a, self.b * other.b)
    def divide(self, other):
        return fraction(self.a * other.b, self.b * other.a)
    def toDecimal(self):
        return self.a / self.b
    def simplify(self):
        for i in range(2, self.a + 1):
            if self.a % i == 0 and self.b % i == 0:
                self.a = self.a // i
                self.b = self.b // i
                break
    def __str__(self):
        return str(self.a) + "/" + str(self.b)
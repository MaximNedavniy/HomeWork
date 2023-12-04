import math


class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        if self.y == other.y:
            res = self.x + other.x
            print(int(res), int(self.y))
            return Fraction(int(res), int(self.y))
        else:
            least_common_multiple = self.y * \
                other.y // math.gcd(self.y, other.y)
            auxiliary_multiplier_1 = least_common_multiple / self.y
            auxiliary_multiplier_2 = least_common_multiple / other.y
            new_x1 = auxiliary_multiplier_1 * self.x
            new_y1 = auxiliary_multiplier_1 * self.y
            new_x2 = auxiliary_multiplier_2 * other.x
            new_y2 = auxiliary_multiplier_2 * other.y
            res = new_x1 + new_x2
            print(int(res), int(new_y2))
            return Fraction(int(res), int(new_y2))

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        if self.y == other.y:
            res = self.x - other.x
            print(int(res), int(self.y))
            return Fraction(int(res), int(self.y))
        else:
            least_common_multiple = self.y * \
                other.y // math.gcd(self.y, other.y)
            auxiliary_multiplier_1 = least_common_multiple / self.y
            auxiliary_multiplier_2 = least_common_multiple / other.y
            new_x1 = auxiliary_multiplier_1 * self.x
            new_y1 = auxiliary_multiplier_1 * self.y
            new_x2 = auxiliary_multiplier_2 * other.x
            new_y2 = auxiliary_multiplier_2 * other.y
            res = new_x1 - new_x2
            print(int(res), int(new_y2))
            return Fraction(int(res), int(new_y2))

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        print(self.x * other.y, self.y * other.x)
        return Fraction(self.x * other.y, self.y * other.x)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        print(self.x * other.x, self.y * other.y)
        return Fraction(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError
        return self.x == other.x and self.y == other.y


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 2)
    print(x + y == Fraction(3, 4))

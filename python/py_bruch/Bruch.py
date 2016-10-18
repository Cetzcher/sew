import math

def ggt(a, b):
    if b == 0:
        return a
    else:
        return ggt(b, a % b)


def kgv(a, b):
    g = ggt(a, b)
    return (a * b) / g


class Bruch(object):

    def __init__(self, *args):
        if len(args) is 1:
            t = args[0]
            if isinstance(t, Bruch):
                self.zaehler = t.zaehler
                self.nenner = t.nenner
            elif isinstance(t, int):
                self.zaehler = t
                self.nenner = 1
            else:
                raise TypeError()
        elif len(args) is 2:
            self.zaehler = args[0]
            self.nenner = args[1]

        if self.nenner is 0:
            raise ZeroDivisionError()
        elif isinstance(self.nenner, float) or isinstance(self.zaehler, float):
            raise TypeError()

    def __int__(self):
        return int(self.zaehler / self.nenner)

    def __float__(self):
        return float(self.zaehler / self.nenner)

    def __complex__(self):
        return complex(self.zaehler / self.nenner)

    def __invert__(self):
        return Bruch(self.nenner, self.zaehler)

    def __eq__(self, other):
        return float(self) == float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __le__(self, other):
        return float(self) <= float(other)

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError()

    def __abs__(self):
        return abs(float(self))

    def __neg__(self):
        return Bruch(-self.zaehler, self.nenner)

    def __str__(self):
        return "({0}{1})".format(abs(self.zaehler), "/" + str(abs(self.nenner)) if self.nenner is not 1 else "")

    def __len__(self):
        return 2

    def __iter__(self):
        return iter([self.zaehler, self.nenner])

    @staticmethod
    def __add(b0, b1):
        # b0 = min, Bruch
        # b1 = max, Bruch
        mi = min(b0, b1)
        mx = max(b0, b1)
        kv = int(kgv(mi.nenner, mx.nenner))
        a = kv // mi.nenner
        b = kv // mx.nenner
        return Bruch(mi.zaehler * a + mx.zaehler * b, kv)

    def __add__(self, other):
        other = Bruch(other)
        return Bruch.__add(self, other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return other + self

    def __sub__(self, other):
        other = -Bruch(other)
        return Bruch.__add(self, other)

    def __rsub__(self, other):
        other = -Bruch(other)
        return self + other

    def __isub__(self, other):
        return other - self

    def __mul__(self, other):
        other = Bruch(other)
        return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return other * self

    def __truediv__(self, other):
        other = Bruch(other)
        return self * ~other

    def __rtruediv__(self, other):
        return Bruch.__truediv__(other, self)

    def __itruediv__(self, other):
        return self / other

"""
b0 = Bruch(3, 2)
b1 = Bruch(1)
print(b0, "+", b1, "=", b0 + b1, "KGV:", kgv(b0.nenner, b1.nenner))
"""
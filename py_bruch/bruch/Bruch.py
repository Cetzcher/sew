
def ggt(a, b):
    if b == 0:
        return a
    else:
        return ggt(b, a % b)


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
        return -(float(self))

    def __str__(self):
        return "({0}{1})".format(abs(self.zaehler), "/" + str(abs(self.nenner)) if self.nenner is not 1 else "")

    def __len__(self):
        return 2

    def __iter__(self):
        return iter([self.zaehler, self.nenner])

    def __add__(self, other):
        if isinstance(other, Bruch):
            kv = ggt(self.nenner, other.zaehler)
            a = self.nenner // kv
            b = other.nenner // kv
            return Bruch(self.zaehler * a + other.zaehler * b, kv)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        if isinstance(other, Bruch):
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)
        else:
            return self * Bruch(other)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return other * self

    def __truediv__(self, other):
        if isinstance(other, Bruch):
            return self * ~other
        return self * ~Bruch(other)

    def __rtruediv__(self, other):
        return Bruch.__truediv__(other, self)

    def __itruediv__(self, other):
        return self / other

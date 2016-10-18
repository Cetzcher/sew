def ggt(a, b):
    """
    Returns the greates common divisor GCD or ggt in german
    :param a: an integer
    :param b: another integer
    :return: the GCD of a and b
    """
    if b == 0:
        return a
    else:
        return ggt(b, a % b)


def kgv(a, b):
    """
    Returns the least common denominator LCD or kgv in german
    :param a: a integer
    :param b: another integer
    :return: the LCD of a and b
    """
    g = ggt(a, b)
    return (a * b) / g


class Bruch(object):
    """
    Represents a Fraction in the form of x / y
    The Fraction utilizes lots of operator overloading it acts as you would expect a fraction to behave
    addition and subtraction find the new deliminator by calculating the LCD of both.
    Every operator returns a new object.
    Beware the Fraction object is mutable, since self.zaehler and self.nenner are exposed as the tests require!

    **How to use**
        :Example:

        >>> b0 = Bruch(1, 2)  # creates a fraction 1 / 2
        >>> b1 = Bruch(1, 4)
        >>> res = b0 + b1     # -> Bruch(3/4)

        >>> b = Bruch(4)      # Bruch(4, 1
        >>> b = Bruch(b0)     # 'copy CTOR'

    """

    def __init__(self, *args):
        """
        Initializes a fraction or Throws errors IF:
            **len(args) == 0 or > 2**                                   ==> Value Error \n
            **len(args) == 1 and args[0] neither int nor fraction**    ==> Type Error \n
            **len(args) == 2 and args[1] == 0**                         ==> Zero Division Error \n
            **len(args) == 2 and args[0 or 1] is not an int**           ==> Type Error \n

        :param args: multiple arguments **either** (int), (int, int), (fraction)
                     if (int) then (int, 1) is assumed.
                     if (fraction) the object will be copied!
        """
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
        else:
            raise ValueError("Only 1 or 2 args allowed got {0}".format(len(args)))

        if self.nenner is 0:
            raise ZeroDivisionError()
        elif isinstance(self.nenner, float) or isinstance(self.zaehler, float):
            raise TypeError()

    def __int__(self):
        """
        Converts to an int
        :return: the integer representation of this fraction object.
        """
        return int(self.zaehler / self.nenner)

    def __float__(self):
        """
        Converts to a float
        :return: the float representation of this fraction object
        """
        return float(self.zaehler / self.nenner)

    def __complex__(self):
        """
        Converts to a Complex number
        :return: the complex representation of this fraction
        """
        return complex(self.zaehler / self.nenner)

    def __invert__(self):
        """
        Flips denominator and numerator
        :return: a flipped fraction
        """
        return Bruch(self.nenner, self.zaehler)

    def __eq__(self, other):
        """
        Tests if self is equal to other
        this is done by using floating point arithmetic
        and due to floating point precision errors this has the same
        problems.
        This method is discouraged due to floating point precision.
        :param other: a object that implements __float__
        :return: true or false
        """
        return float(self) == float(other)

    def __gt__(self, other):
        """
        Tests whether other is greater than self
        :param other: a object that implements __float__
        :return: True or False
        """
        return float(self) > float(other)

    def __lt__(self, other):
        """
        Tests whether other is less than self
        :param other: a object that implements __float__
        :return: True or False
        """
        return float(self) < float(other)

    def __ge__(self, other):
        """
        Tests whether other is greater than or equal to self
        :param other: a object that implements __float__
        :return: True or False
        """
        return float(self) >= float(other)

    def __le__(self, other):
        """
        Tests whether other is less than or equal to self
        :param other: a object that implements __float__
        :return: True or False
        """
        return float(self) <= float(other)

    def __pow__(self, power, modulo=None):
        """
        Returns the fraction raised to power 'power'
        :param power: the power to which the fraction is raised.
        :param modulo: unused
        :return: this fraction raised to power.
        """
        if isinstance(power, int):
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError()

    def __abs__(self):
        """
        The absolute value of this
        :return: the abs(float(self)) value
        """
        return abs(float(self))

    def __neg__(self):
        """
        multiplies the enumerator by -1
        :return: the negated fraction
        """
        return Bruch(-self.zaehler, self.nenner)

    def __str__(self):
        """
        The string representation of this fraction
        :return: (numerator/deliminator) as a string
        """
        return "({0}{1})".format(abs(self.zaehler), "/" + str(abs(self.nenner)) if self.nenner is not 1 else "")

    def __len__(self):
        """
        Length of this object in order to treat it as a sequence for
        assignment destructuring like a, b = fraction.
        :return: the const value 2
        """
        return 2

    def __iter__(self):
        """
        an iterator on the fraction in sequence representation
        :return: the iterator
        """
        return iter([self.zaehler, self.nenner])

    @staticmethod
    def __add(b0, b1):
        """
        Private helper method for adding 2 fractions.
        :param b0: a Fraction
        :param b1: a Fraction
        :return: The resulting Fraction with the denominator being the LCD of b0, b1
        """
        # b0 = min, fraction
        # b1 = max, fraction
        mi = min(b0, b1)
        mx = max(b0, b1)
        kv = int(kgv(mi.nenner, mx.nenner))
        a = kv // mi.nenner
        b = kv // mx.nenner
        return Bruch(mi.zaehler * a + mx.zaehler * b, kv)

    @staticmethod
    def __makeBruch(value):
        """
        Creates a fraction from a value
        :param value: either a fraction or a integer
        :return: a fraction or throws an error if
        """
        return Bruch(value)

    def __add__(self, other):
        """
        Adds self and other see __add
        :param other: a fraction or an integer raises errors see __init__
        :return: a Fraction
        """
        other = Bruch(other)
        return Bruch.__add(self, other)

    def __radd__(self, other):
        """
        Reflected add see __add__
        :param other: see __add__
        :return: returns a fraction
        """
        return self + other

    def __iadd__(self, other):
        """
        see __add__
        :param other: see __add__
        :return: a fraction
        """
        return other + self

    def __sub__(self, other):
        """
        Negates other and adds it to self, see __add__
        :param other: a fraction or number, see __init__
        :return: a fraction
        """
        other = -Bruch(other)
        return Bruch.__add(self, other)

    def __rsub__(self, other):
        """
        see __sub__
        :param other: see __sub__
        :return: a fraction
        """
        return -self + other

    def __isub__(self, other):
        """
        see __sub__
        :param other: see __sub__
        :return: a fraction
        """
        return self - other

    def __mul__(self, other):
        """
        Multiplies self with other
        :param other: a fraction or int, see __init__
        :return: a fraction
        """
        other = Bruch(other)
        return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)

    def __rmul__(self, other):
        """
        Reflected multiplication
        :param other: see __mul__
        :return: a fraction
        """
        return self * other

    def __imul__(self, other):
        """
        see __mul__
        :param other: see __mul__
        :return: a fraction
        """
        return other * self

    def __truediv__(self, other):
        """
        returns self divided by other this is done by inverting fraction
        :param other: a fraction or an integer, see __int__
        :return:
        """
        other = Bruch(other)
        return self * ~other

    def __rtruediv__(self, other):
        """
        see __truediv__
        :param other: see __truediv__
        :return: a fraction
        """
        return Bruch.__truediv__(other, self)

    def __itruediv__(self, other):
        """
        see __truediv__
        :param other: see __truediv__
        :return: a fraction
        """
        return self / other
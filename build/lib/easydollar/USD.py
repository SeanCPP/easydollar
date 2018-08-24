"""
USD.py | US Dollar\n
Light-weight data type for accurate USD-based calculations
"""


import math

class USD:
    """This data type represents the United States Dollar without using any floating-point arithmetic."""

    # Magic Methods
    ################################################

    def __init__(self, dollars=0, cents=0):
        self.cents = cents + (dollars * 100)
    
    def __add__(self, other):
        cents = self.cents + other.cents
        return USD(cents=cents)
    
    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        cents = self.cents - other.cents
        return USD(cents=cents)
    
    def __isub__(self, other):
        return self - other

    def __mul__(self, scalar):
        if scalar % 1 == 0:
            cents = self.cents * scalar
            return USD(cents=cents)
        raise ValueError('scalar value must be a whole number.')
    
    def __imul__(self, scalar):
        return self * scalar

    def __truediv__(self, div):
        if div % 1 == 0:
            return self.distribute(div)[0]
        raise ValueError('divisor must be a whole number.')
    
    def __idiv__(self, div):
        self.cents = (self / div).cents
        return self

    def __lt__(self, other):
        return self.cents < other.cents

    def __le__(self, other):
        return self.cents <= other.cents

    def __gt__(self, other):
        return self.cents > other.cents
    
    def __ge__(self, other):
        return self.cents >= other.cents

    def __float__(self):
        d, c = self.__parsecents()
        return float(f'{d}.{c}')
    
    def __repr__(self):
        d, c = self.__parsecents()
        return f'USD(dollars={d}, cents={c})'

    def __str__(self):
        dollar, cent = self.__parsecents()
        return f'${dollar:,d}.{cent:02d}'
    
    
    # Public Methods
    ###################################
    
    def raw_str(self):
        d, c = self.__parsecents()
        return f'{d}.{c:02d}'

    def with_interest(self, percent):
        """ Returns a new USD with interest applied. """
        temp = self
        temp.apply_interest(percent)
        return temp

    def apply_interest(self, percent):
        """ Applies interest percentage to the current instance. """
        percent /= 100
        interest_cent = round(self.cents * percent)
        self.cents += interest_cent

    def interest(self, percent):
        """ Returns a new USD of the interest amount. """
        percent /= 100
        return USD(cents=round(self.cents * percent))

    def distribute(self, n):
        """ Returns a list of USDs such that each element could be added together to get the original value.
        """
        low = math.floor(self.cents / n)

        high = low + 1

        num_highs = self.cents % n
        num_lows = n - num_highs
        
        lows = [USD(cents=low) for _ in range(num_lows) ]
        highs = [USD(cents=high) for _ in range(num_highs)]

        return highs + lows


    # Private Methods
    #################################################
    
    def __parsecents(self):
        """Translate cents to dollars\n
        returns tuple (dollars, remaining_pennies) """
        dollars = math.floor(self.cents / 100)
        pennies = self.cents % 100
        return (dollars, pennies)


def usd(s):
    """This is the recommended way to construct USD objects.
    Example arguments: 
    1. '50.67' 
    2. '100'
    3. '$0.500'
    4. '$5,000.99'
    """
    if ',' in s:
        s = s.replace(',', '')
    if '$' in s:
        s = s.replace('$', '')

    if not '.' in s:
        try:
            return USD(dollars=int(s))
        except Exception:
            raise ValueError('Argument must be a str of a dollar amount.')
    else:
        dollars, cents = s.split('.')
        try:
            return USD(int(dollars), int(cents))
        except Exception:
            raise ValueError('Argument must be a str of a dollar amount.')
import math
import re

class fraction(float):
    fraction_pattern = re.compile('^(([-+]?[0-9]+[/])?([-+]?[0-9]+[/])?[1-9][0-9]*)$')
    
    def __init__(self, f = 0.0, n = 0, d = 1):
        number = f + n / d
        self.denomanator = int(10 ** len(str(number).partition('.')[-1]))
        self.numerator = int(number * self.denomanator)
        self.simplify()
        negative = self.numerator < 0
        self.numerator = int(abs(self.numerator))
        self.whole = int(self.numerator // self.denomanator)
        self.numerator -= (self.denomanator * self.whole)
        if negative:
            if self.whole > 0 :
                self.whole = -self.whole
            else:
                self.numerator = -self.numerator
        
    def simplify(self):
        g = math.gcd(self.numerator, self.denomanator)
        self.numerator /= g
        self.denomanator /= g
        
    def __str__(self):
        wh = str(int(self.whole))+"/" if self.whole != 0 else ''
        num = str(int(self.numerator)) +"/" if self.numerator != 0 else ''
        den = str(int(self.denomanator)) if self.denomanator != 1 else ''
        return "%s%s%s" % (wh, num, den)
    
    def __repr__(self):
        w = str(self.whole)+"/" if self.whole != 0 else ''
        return "fraction[%s%d/%d]" % (w, self.numerator, self.denomanator)

def to_fraction(s:str):
    return fraction(eval(s))

def to_float(frc:fraction):
    return (frc.denomanator * frc.whole + frc.numerator) / frc.denomanator
    
def is_fraction(frc:str):
    return bool(fraction.fraction_pattern.search(frc))
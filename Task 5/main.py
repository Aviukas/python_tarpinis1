# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos
from modules.math.composition import *
from modules.math.division import *
from modules.math.subtraction import *
from modules.math.multiplication import *
from modules.numbers.numbers import *

def addition(a, b):
    return composition(a, b)
    
def divivsion(a, b):
    return division(a, b)


# Kitų failų ir žemiau esančio kodo nekeiskite
a = addition(one, four);
b = divivsion(four, two);
c = substraction(three, two);
d = multiplication(five, two);

print(a);
print(b);
print(c);
print(d);

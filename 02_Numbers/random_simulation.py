import math
import random

print(math.floor(3.65))
print(math.floor(-4.2))
print(math.trunc(5.9))
print(math.trunc(-6.7))

random_num = random.randint(1,10)
print(random_num)
range = random.randrange(10,100)
print(range)

language = ['Python','C++','C','Java']
print(random.choices(language))

dice = [1,2,3,4,5,6]
random.shuffle(dice)
print(dice)

from decimal import Decimal
sum = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.2')
print(sum)

from fractions import Fraction
Fra = Fraction(9,3)
print(Fra)
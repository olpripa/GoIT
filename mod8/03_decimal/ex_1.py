"""
Необхідність використання. Налаштування точності
"""

from decimal import Decimal, getcontext

f = 0.2 + 0.1 + 0.3 - 0.5
print(f)
print(Decimal(str(f)))

f_dec = Decimal('0.2') + Decimal('0.1') + Decimal('0.3') - Decimal('0.5')
print(f_dec)
not_precision = Decimal('1') / Decimal('3')
print(not_precision)
getcontext().prec = 6
not_precision = Decimal('1') / Decimal('3')
print(not_precision)
not_precision = Decimal('11') / Decimal('3')
print(not_precision)


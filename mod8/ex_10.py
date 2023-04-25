"""
defaultdict: Зручно, якщо ми розбиваємо на різні списки набори телефонних операторів
"""

from collections import defaultdict

phone_numbers = ['0509993636', '0679993636', '0959993636', '0969993636',
                 '0509993637', '0639993636', '0509993632', '0339993632']

phone_operator_numbers = defaultdict(list)
# {'Vodafone': ['0509993636', '0959993636', ..., 'Life'}

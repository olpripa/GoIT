# def taxer(base_tax):
#     def calculate(money):
#         nonlocal base_tax
#         # print(base_tax)
#         if money > 10000:
#             base_tax = 1.5 * base_tax  # міняємо ставку оподаткування
#             # print(f'base_tax: {base_tax}')
#         return money - base_tax * money
#     return calculate

def taxer_simple(base_tax, money):
    if money > 10_000:
        base_tax = 1.5 * base_tax
    return money - base_tax * money


money_ukr = taxer_simple(0.1, 5000)
money_swd = taxer_simple(0.55, 25000)
print(money_ukr, money_swd)

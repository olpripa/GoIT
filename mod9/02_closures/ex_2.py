# Closures

def taxer(base_tax):
    def calculate(money):
        nonlocal base_tax
        # print(base_tax)
        if money > 10000:
            base_tax = 1.5 * base_tax  # міняємо ставку оподаткування
            # print(f'base_tax: {base_tax}')
        return money - base_tax * money
    return calculate


ukr = taxer(0.1)
m_u = ukr(5000)


swd = taxer(0.55)
m_s = swd(25000)
m_s_1 = swd(2500)


print(m_u, m_s, m_s_1)
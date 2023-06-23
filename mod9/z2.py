DEFAULT_DISCOUNT = 0.05
customer_0 = {"name": "Dima"}
customer_1 = {"name": "Boris", "discount": 0.15}
customer_3 = {"name": "Olga", "discount": 0}


def get_discount_price_customer(price, customer):
    global DEFAULT_DISCOUNT

    if customer.get('discount') == None:
        discount = DEFAULT_DISCOUNT
    else:
        discount = customer.get('discount')
    return price * (1 - discount)


print(get_discount_price_customer(100, customer_0))
print(get_discount_price_customer(100, customer_1))
print(get_discount_price_customer(100, customer_3))

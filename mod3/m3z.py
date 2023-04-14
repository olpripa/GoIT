# ## Завдання 2 
# def invite_to_event(username):
#     return f"Dear {username}, we have the honour to invite you to our event"

# print(invite_to_event('Oleksandr'))


# ##Завдання 3 Вартість таксі із збільшення лічильника поїздо global змінні
# base_rate = 40
# price_per_km = 10
# total_trip = 0

# def trip_price(path):
#     global total_trip
#     total_trip += 1
#     return base_rate + price_per_km * path

# print(trip_price(50))
# print(total_trip)

# ##Завдання 4 
# def discount_price(price, discount):
#     def apply_discount():
#         nonlocal price
#         price -= price * discount
#     apply_discount()
#     return price

# print(discount_price(100,0.1))

# ## Завдання 5
# def get_fullname(first_name, last_name, middle_name=''):
#     if middle_name == '':
#         return f'{first_name} {last_name}'
#     else:
#         return f'{first_name} {middle_name} {last_name}'


# print(get_fullname(first_name='Oleksandr', last_name='Pripa', middle_name='Vas'))

# ## Завдання 6
# def format_string(string, length):
#     if len(string) == length:
#         format_string = string
#     else:
#         sp = (length - len(string)) // 2
#         format_string = ' ' * sp + string
#     return format_string


# print(format_string(string='aaaaaaaaaaaaaaaaac', length=12))
# print(format_string(length=15, string='abaa'))

# ## Завдання 7
# def first(size, *args):
#     size += len(args)
#     return size

# def second(size, **kwargs):
#     size += len(kwargs)
#     return size

# print(first(5, "first", "second", "third"))
# print(first(1, "Alex", "Boris"))
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))
# print(second(10, comment_one="Alex", comment_two="Boris"))

# ## Завдання 8
# def cost_delivery(quantity, *_, discount=0):
#     cost_delivery = 5
#     if quantity >= 2:
#         cost_delivery = cost_delivery + (quantity - 1) * 2
#     cost_delivery -= cost_delivery * discount
#     return cost_delivery

# print(cost_delivery(2, 1, 2, 3))
# print(cost_delivery(3, 3))
# print(cost_delivery(1))
# print(cost_delivery(2, 1, 2, 3, discount=0.5))

# def cost_delivery(quantity, *_, discount=0):
#     """Функція повертає суму за доставлення замовлення.
    
#     Перший параметр &mdash; кількість товарів в замовленні.
#     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""

#     result = (5 + 2 * (quantity - 1)) * (1 - discount)
#     return result

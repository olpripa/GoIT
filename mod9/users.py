def greet_users(names):
    """Виведення привітання для кожного користувача у списку."""
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)


if __name__ == '__main__':
    usernames = ['alex', 'jack', 'anna']
    greet_users(usernames)

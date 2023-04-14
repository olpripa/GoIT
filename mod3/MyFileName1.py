def hello(text: str):
    print(f'Hello -> {text}')


if __name__ == "__main__":
    print('First line before call func')
    hello('call func')
    hello(True)
    print('Second line after call func')

    print(__name__)
# Функція приймає рядок, а повертає словник, де ключ це символ рядка, а значення код ASCII
# {'key': 'value'}

def codes_of_string(text: str) -> dict:
    codes = {}
    for symbol in text:
        if not symbol in codes:
            codes[symbol] = ord(symbol)

    return codes

print(codes_of_string('Hello world'))
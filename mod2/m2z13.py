import string

message = input("Введіть повідомлення: ")
offset = int(input("Введіть зсув: "))
encoded_message = ""
pos_a = ord('a')
pos_A = ord('A') 

for ch in message:
    if ch in string.ascii_lowercase:
        pos = ord(ch) - pos_a
        pos = (pos + offset) % 26
        new_ch = chr(pos + pos_a)
        encoded_message += new_ch
    elif ch in string.ascii_uppercase:
        pos = ord(ch) - pos_A
        pos = (pos + offset) % 26
        new_ch = chr(pos + pos_A)
        encoded_message += new_ch
    else:
        encoded_message += ch
print(f'введено : {message}, новий {encoded_message}')
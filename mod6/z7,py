def sanitize_file(source, output):
    with open(source,'r') as fh:
        txt = fh.read()
    txt_n = txt.replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace(
        '5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '')
    with open(output,'w') as fh:
        fh.write(txt_n)


sanitize_file('recept.txt', 'test.txt')

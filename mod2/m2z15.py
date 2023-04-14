result = None
operand = None
operator = None
wait_for_number = True
operator_list = ['+','-','*','/','=']

while True:
    if wait_for_number:
        try:
            operand = float(input('>>>'))
            wait_for_number = False
            
            if result == None:
                result = operand
            else:
                if operator == "+":
                    result += operand
                if operator == "-":
                    result -= operand
                if operator == "/":
                    try:
                        result /= operand
                    except ZeroDivisionError:
                        print('number is 0')
                        wait_for_number = True
                        continue
                if operator == "*":
                    result *= operand
        except ValueError:
            print('wait number')
            continue
    elif not wait_for_number:
        operator = input('>>>')
        if operator not in operator_list:
            print('очікую на оператор')
            continue
        elif operator == '=':
            break      
        else:
            wait_for_number = True

print(result)
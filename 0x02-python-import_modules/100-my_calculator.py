#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    if operator not in '*+-/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = sys.argv[1]
    b = sys.argv[3]
    if operator == '+':
        result = add(int(a), int(b))
    elif operator == '-':
        result = sub(int(a), int(b))
    elif operator == '*':
        result = mul(int(a), int(b))
    else:
        result = div(int(a), int(b))
    print("{} {} {} = {}".format(a, operator, b, result))

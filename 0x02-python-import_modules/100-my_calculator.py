#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    op_functions = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
        }
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    elif sys.argv[2] not in op_functions.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        ans = op_functions[op](a, b)
        print("{} {} {} = {}".format(a, op, b, ans))

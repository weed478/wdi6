def print_vars(var):
    for k, v in var.items():
        print(k, "=", v)


def sanitize(expr):
    return expr.replace(" ", "").lower()


operators = [
    '^',
    '*',
    '/',
    '+',
    '-',
]


def to_rpn(expr):
    expr = sanitize(expr)

    rpn = []
    operator = None

    i = 0
    while i < len(expr) and expr[i] != ")":
        if expr[i].isalpha():
            # is variable name
            rpn.append(expr[i])

        elif expr[i].isnumeric():
            # is constant
            n = int(expr[i])
            while i + 1 < len(expr) and expr[i + 1].isnumeric():
                i += 1
                n *= 10
                n += int(expr[i])

            rpn.append(n)

        elif expr[i] in operators:
            # is operator
            if expr[i] == "-" and (operator is not None or len(rpn) == 0):
                # unary minus
                rpn.append(0)

            operator = expr[i]

        elif expr[i] == "(":
            # nested expression
            nested_ex, n = to_rpn(expr[i+1:])
            i += n
            rpn.append(nested_ex)

        else:
            print("WTF happened")
            exit(1)

        if operator is not None and len(rpn) >= 2:
            # operator has 2 args
            b = rpn.pop()
            a = rpn.pop()
            rpn.append((a, b, operator))
            operator = None

        i += 1

    # end of expression
    if len(rpn) == 1:
        return rpn[0], i + 1
    else:
        print(":(")
        exit(1)


def parse_value(val, var):
    if type(val) == tuple:
        return parse_rpn(val, var)
    elif type(val) == str:
        return var[val]
    else:
        return int(val)


def parse_rpn(expr, var):
    a = parse_value(expr[0], var)
    b = parse_value(expr[1], var)

    op = expr[2]
    if op == "+":
        return a + b

    elif op == "-":
        return a - b

    elif op == "*":
        return a * b

    elif op == "/":
        return a / b

    elif op == "^":
        return a ** b


variables = {
    "x": 2,
    "y": 3,
    "z": 5,
}
print_vars(variables)

ex = None
while ex != "":
    ex = input("> ")
    rpn, _ = to_rpn(ex)
    print(ex, "=", parse_rpn(rpn, variables))

from art import logo


# Add
def add(a1, a2):
    return a1 + a2


# Subtract
def subtract(s1, s2):
    return s1 - s2


# Multiply
def multiply(m1, m2):
    return m1 * m2


# Divide
def divide(d1, d2):
    return d1 / d2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    continue_math = True

    while continue_math:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        function = operations[operation_symbol]
        answer = function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation.: ") == "y":
            num1 = answer
        else:
            continue_math = False
            calculator()


calculator()

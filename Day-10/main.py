from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# addin = operations["+"]
# print(addin(1, 2))


def calculator():
    print(logo)
    playing = True

    num1 = float(input("What is your first number?: "))

    while playing:
        operation_choice = input("+\n-\n*\n/\nPick an operation: ")  # Can for loop through the symbols from operations
        num2 = float(input("What is your next number?: "))

        answer_function = operations[operation_choice]

        answer = round(answer_function(num1, num2), 10)
        print(f"{num1} {operation_choice} {num2} = {answer}")

        num1 = answer
        go_on = input(f"Type 'y' to continue calculating with {answer}, "
                      f"or type 'n' to start a new calculation: ").lower()
        if go_on == 'n':
            calculator()


calculator()

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


dict_operations = {"+": add, "-": subtract, "/": divide, "*": multiply}


def calculator():
    is_result_reused = "y"
    first_number = float(input("What's the first number?: "))
    while is_result_reused == "y":
        for key in dict_operations:
            print(key)
        operation = input("Pick an  operation: ")
        second_number = float(input("What's the next number?: "))

        result = dict_operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        is_result_reused = input(f"Type 'y to continue calculating with {result}, "
                                 f"or type 'n' to start a new calculation or type 'q' to exit: ").lower()
        first_number = result
    if is_result_reused == "n":
        calculator()
    elif is_result_reused == "q":
        exit()
    else:
        print("Invalid input. quitting...")
        exit()



calculator()

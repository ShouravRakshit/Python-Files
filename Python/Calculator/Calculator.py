from os import system, name
from art import logo

# Created a function that can clean the terminal.
def clear():

	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2 

def divide(n1, n2):
    return n1 / n2 

def multiply(n1, n2):
    return n1 * n2 

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculation(num1):
    operation_symbol = input("Pick an operation ")
    num2 = int(input("What's the next number?: "))


    calc_function = operations[operation_symbol]
    answer = calc_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    new_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

    if new_calc == 'y':
        calculation(answer)

    elif new_calc == 'n':
        clear()
        show_operations()

    else:
        print("Wrong input")

def show_operations():
    print(logo)
    num1 = int(input("What's the first number?: "))

    for key in operations:
        print(key)

    calculation(num1)

show_operations()
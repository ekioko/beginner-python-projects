from calc_art import logo
#Calculator
print(logo)
#add function
def add(num1, num2):
    return num1 + num2
#subtract function
def subtract(num1, num2):
    return num1 - num2
#multiply function
def multiply(num1, num2):
    return num1 * num2
#divide function
def divide(num1, num2):
    return num1 / num2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
  calc_on = True
  num1 = int(input("What's the first number?: "))
  for item in operations:
      print(item)
  while calc_on:
    operator = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))

    #user input first number
    result = operations[operator](num1, num2)

    print(f"{num1} {operator} {num2} = {result}")

    more_calc = input("'y' to continue calculating with the result, 'n' to start a new calculation. If you are finished with the calculator, type 'stop'")
    if more_calc == 'y':
      num1 = result
    elif more_calc == 'n':
      calc_on = False
      calculator()
    else:
      calc_on = False

calculator()

'''b) Write a program using match case that simulates a simple calculator.
1. Ask the user for two numbers and an operation (+, -, *, /).
2. Perform the operation using match case .'''
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
opr = input("What you want to do (+,-,*,/): ")
match opr :
    case "+" :
        print("The sum is: ", num1 + num2)
    case "-" :
        print("The difference is: ", num1 - num2)
    case "*" :
        print("The product is: ", num1 * num2)
    case "/" :
        print("The quotient is: ", num1 / num2)

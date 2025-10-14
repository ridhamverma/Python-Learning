a = int(input("Enter a number(1-10): "))

match a :
    case 1:
        print("You won a charger")
    case 3:
        print("The won $3")
    case 6:
        print("You won a camera")
    case _:
        print("Better luck next time")
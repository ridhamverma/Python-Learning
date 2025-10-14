'''a) Ask the user to enter a day number (1-7) and print the corresponding day of
the week using match case .'''
day = int(input("Enter a day(1-7): ")) # 1 - Monday, 2 - Tuesday, 3 - Wednesday, 4- Thursday, 5 - Friday, 6 - Saturday, 7 - Sunday.
match day : 
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thurday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _ :
        print("!")
''' Take a user input string and check if it is a palindrome (same forwards and backwards).'''
input = input("Enter a string: ")

if input == input[::-1]:
    print("It is a palindrome")
else :
    print("It is not a palindrome")

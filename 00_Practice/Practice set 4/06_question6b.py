'''2. Take a user input string and check if it is a palindrome (same forwards and
backwards).'''

string = input("Enter a string: ")

string = string.replace(" ", "").lower()

if(string == string[::-1]):
    print("It is a palindrome")

else:
    print("It is not a palindrome")
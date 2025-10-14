'''b) Write a program that keeps asking the user to enter a password until they
enter the correct one.'''
correct_password = "9148q" # Correct password

user_input = input("Enter password: ") # Taking password as input from user

while (user_input != correct_password): 
    print("Incorrect password! Try again: ") 
    user_input = input("Enter password: ")

print("Correct Password! Access granted...")


'''b) Create a program that checks if a person is eligible to vote (age >= 18).'''
age = int(input("Enter your age: "))
if (age >=18):
    print("You are eligible to vote")
elif (age == 0):
    print("Kid! You are just born")
else:
    print("You are not eligible to vote")
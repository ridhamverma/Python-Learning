'''b) Print the multiplication table of a number (entered by user).'''
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num,"x", i, "=", num*i)
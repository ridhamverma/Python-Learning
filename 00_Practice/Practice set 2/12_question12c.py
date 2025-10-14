'''b) Use a while loop to reverse a given number (e.g., 123 → 321). '''
number = int(input("Enter a number: "))

rev = 0
while number > 0:
    digit = number % 10        # get the last digit
    rev = rev * 10 + digit     # add it to reversed number
    number = number // 10      # remove last digit from number

print("Reversed number is:", rev)
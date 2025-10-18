''' Create a string variable name with your full name. Print:
1. The first character
2. The last character
3. The length of the string

Concatenate two strings: "Hello" and "World" with a space in between.'''

name = "Ridham"
print(name[0]) # Prints the first character
print(name[5]) # Prints the last character
print(len(name)) # Prints the length of the string

# Concatenating two strings 
str1 = "Hello"
str2 = "World"

# Method 1:
# result = str1 +" "+ str2
# print(result)

# Method 2:
result =" ".join([str1, str2])
print(result)
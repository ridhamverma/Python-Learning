s = "Hello World" #String are immutable

# name [0] = "H" #You cannot do this

a = len(s)
# print(a)
# print(s.upper()) # Converts string to upper case
# print(s.lower()) # Converts string to lower case
# print(s.capitalize()) # Converts only first word to upper case
# print(s.title()) # Converts only first letter of words to upper case

# text = " \nhello world "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip()) # Output: "hello world "
# print(text.rstrip()) # Output: " hello world"

# text = "Python is fun and fun and fun and fun"
# print(text.find("is")) # Output: 7 Index of first occurance
# print(text.replace("fun", "awesome"))

# text = "apple,banana,orange"
# print(text.split(","))
# print(",".join(['apple', 'banana', 'orange']))

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: False



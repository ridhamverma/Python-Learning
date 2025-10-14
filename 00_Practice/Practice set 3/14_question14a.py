'''Given text = "Python Programming" , do the following:
1. Print the first 6 characters
2. Print the last 6 characters
3. Print every second character from the string 
Reverse the string text using slicing.'''

text = "Python Programming"
print(len(text))
print(text[0:6])
print(text[-6: ])
print(text[0:18:2])
reversed_text = text [::-1]
print(reversed_text)
'''Take the string " i love python programming " and:
1. Remove extra spaces from both ends
2. Convert it to title case
3. Count how many times "o" appears

Check if the string "123abc" is alphanumeric.'''

str = " i love python programming "
print(str.strip()) # Removes extra spaces from both ends
print(str.title()) # Convert it to title case
print(str.count("o")) # output: 3 

print(str.isalnum()) # Output: False

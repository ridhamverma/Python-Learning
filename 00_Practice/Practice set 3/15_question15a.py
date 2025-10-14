'''Take the string " i love python programming " and:
1. Remove extra spaces from both ends
2. Convert it to title case
3. Count how many times "o" appears '''

str = " i love python programming "
s = str.strip()
print(s)
print(s.title()) 
print(s.find("o"))


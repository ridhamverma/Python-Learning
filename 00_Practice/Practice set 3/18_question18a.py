'''Write a program that counts how many vowels are in a given string.'''
sentence = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in sentence:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)


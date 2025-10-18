'''1. Write a program that counts how many vowels are in a given string. '''

sentence = input("Enter a word or sentence: ")

vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print("Number of vowels: ", count)




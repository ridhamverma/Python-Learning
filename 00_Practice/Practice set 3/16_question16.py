'''Using format() , create a sentence:
1. "My name is John and I am 25 years old."
by passing "John" and 25 as variables.
2. Do the same using f-strings.'''
sentence = "My name is {} and I am {} years old."
a = "John"
b = 25
s1 = sentence.format(a, b)
print(s1)

print(f"My name is {a} and I am {b} years old.")
age = int(input("Enter your age: "))

if(age>18):
    print("You can drive")
elif(age==18):
    print("Lets schedule an interview")
elif(age == 0):
    print("Hey Kid! You are just born")
else:
    print("You cannot drive")

print("End of program")
age = int(input("Enter your age: "))
if 18 <= age <= 100:
    print("Yes , You can Vote Now!")

elif age <= 18:
    print("you have to grow up!")

elif age >= 100:
    print("Sorryyy , You are near to death!")

else:
    print("Invalid age") # it handles the invalid statements

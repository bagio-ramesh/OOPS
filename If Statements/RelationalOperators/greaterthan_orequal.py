num1 =int(input("Enter any number: "))
num2 = int(input("Enter any number: "))
num3 = int(input("Enter any number: "))


if num1 > num2 and num1 > num3:
    print(f"{num1}Num1 is Greater")

elif num2 > num1 and num2 > num3:
    print(f"{num2} num2 is Greater")

elif num3 > num1 and num3 > num2:
    print(f"{num3} num3 is Greater")
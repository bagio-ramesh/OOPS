num1 = int(input("Enter any number: ")) # 45
num2 = int(input("Enter any number: ")) # 67
num3 = int(input("Enter any number: ")) # 88

# Find the second largest
if (num1 >= num2 and num1 <= num3) or (num1 >= num3 and num1 <= num2):
    print(f"Second largest is :{num1}")

elif (num2 >= num1 and num2 <= num3) or (num2 >= num3 and num2 <= num1):
    print(f"Second largest is :{num2}") # 67

else:
    print(f"Second largest Number is :{num3}")
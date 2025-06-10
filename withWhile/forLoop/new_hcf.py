num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter Your 2nd number: "))

if num1 > num2:
    smallest = num2

else:
    smallest = num1

hcf = 1 

for i in range (1,smallest+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print(f"Hcf:{hcf}")

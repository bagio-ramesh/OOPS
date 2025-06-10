def min_two(num1,num2):
    if num1 > num2:
        return num2
    else:
        return num1

numm1 = int(input("Enter 1st number: "))
numm2 = int(input("Enter 2nd number: "))
res = min_two(numm1,numm2)
print(f"smallest number is {res}")
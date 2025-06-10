def smart_sub(num1,num2):
    if num1 > num2:
        return num1 -  num2
    else:
        return num2 - num1
numm1 = int(input("ENTER 1ST NUMBER: "))
numm2 = int(input("ENTER 2ND NUMBER: "))

result = smart_sub(numm1,numm2)
print(result)



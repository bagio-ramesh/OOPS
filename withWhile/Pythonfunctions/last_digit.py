def last_digit(num1,num2):
    if num1 % 10 > num2 % 10:
        return num1
    
    else:
        return num2
n1 = int(input("Enter 2 numbers"))
n2 = int(input())   
res = last_digit(n1,n2)
print(res)
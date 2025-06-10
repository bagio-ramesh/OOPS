num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter Your 2nd number: "))
hcf = 0


for i in range(1,num1+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf=i
print(hcf)
    
    
        

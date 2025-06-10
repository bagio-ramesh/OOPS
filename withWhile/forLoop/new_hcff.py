num1 = int(input("Enter your first number: "))  #16
num2 = int(input("Enter your second number: ")) # 32


largest_num = num1 if num1 > num2 else num2  # return num1 if num1 > num2 else return num2
smallest_num = num1 if num1 < num2 else num2
hcf = 1 

for i in range(1, smallest_num + 1):  # We only need to check up to the smaller number
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
        print(i)

print(f"HCF: {hcf}")  # Moved outside the loop to print only the final result
#print(f"Largest num :{largest_num}") 
#print(f"Smallest num:{smallest_num}")
num = int(input("Enter Any Number: ")) # 428
i = 1
sum = 0

while i <= num:
    last_digit = num % 10
    qube = last_digit ** 3
    sum = sum + qube
    num = num // 10 
print(sum)
    

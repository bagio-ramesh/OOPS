num = int(input("Enter any number: ")) # 3
result = 0
sum = 0

for i in range(1,num+1): #(1,3)
    result = result*10+num
    sum = sum + result
print(sum)
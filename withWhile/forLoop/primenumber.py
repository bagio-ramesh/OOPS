num = int(input("Enter any number: "))
prime = "Yea it is"

for i in range(2,num):
    if num%i == 0:
        prime = "No Its not"
        break
print(prime)
def factorial(num):
     result = 1
     for i in range(1,num+1):
          result = result *i
     return result
number = int(input("Enter any number: "))
res = factorial(number)
print(res)
     

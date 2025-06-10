num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2st number: "))

try:
    division_res = num1/num2
    print(division_res)
    
except Exception as e:
    num2 = int(input("Enter 2st number again: "))

try:
    division_res = num1 / num2
    print(division_res)

except Exception as e:
    print(e)

finally:
    print("Program Completed")


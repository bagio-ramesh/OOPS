num = int(input("Enter Any Number: ")) # 6
if num % 2 == 1: # false
    print("Weird")

elif num % 2 == 0 and 2 <= num <=5: #  false
    print("Not Weird")

elif num % 2 == 0 and 6 <= num <= 20: # true , exit the program
    print("Weird")

elif num % 2 == 0 and num > 20: # 
    print("Not Weird")

else:
    print("No More Option")

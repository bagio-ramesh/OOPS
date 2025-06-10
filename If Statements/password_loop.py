real_password = "Bagio@4321"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    input = input("Enter Your Password Broo!: ")
    if input == real_password:
        print("Login Successfully Completed!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Wrong Password Broo {remaining} attemps remaining!")
else:
    print("Your Account Locked Due To Too Many Failed Attempts Try After 3 Minutes Asap!")
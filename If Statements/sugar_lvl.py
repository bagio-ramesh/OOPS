sugar_lvl = int(input("Enter your current Sugar Lvl:" ))

if sugar_lvl < 75:
    print("Low Sugar")

elif sugar_lvl < 100:
    print("Nomal") 

elif sugar_lvl <= 125:
    print("Prediabetic")

else:
    print("Diabetic")

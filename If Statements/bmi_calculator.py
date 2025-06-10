age = int(input("Enter your Current Age: "))
height = int(input("Enter Your Height in (Cm): "))
weight = int(input("Enter your Weight in (kg): "))
height_in_meter = height / 100
bmi = weight / height_in_meter ** 2
if bmi <= 18.5:
    print(f"{bmi}::UnderWeight")

elif bmi <= 24.9:
    print(f"{bmi}::Normal Weight")   

elif bmi <= 29.9:
    print(f"{bmi}::OverWeiight")

elif bmi <= 34.9:
    print(f"{bmi}::Obesity\nClass1.")

elif bmi <= 39.9:
    print(f"{bmi}::Obesity\nClass2.")

else:
     print(f"{bmi}::Obesity\nClass3.")








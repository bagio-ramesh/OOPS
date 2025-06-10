romans = {"I":1,"V":5,"X":10}

print(romans["V"])

romans["L"]=50
print(romans)

romans["C"]=100
print(romans)

if "D" not in romans:
    romans["D"] = 150
    print(romans)


if "D" in romans:
    print("Exist")

else:
    print("Not Exist")


if "M"  not in romans:
    romans["M"]=1000

print(romans)


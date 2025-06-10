temparature = int(input("Enter the room temperature: "))

if temparature < 15:
    print(f"{temparature} is damn cool")

elif temparature <  20:
    print(f"{temparature} is cool")

elif temparature < 25:
    print(f"{temparature} is warm")

elif temparature < 30:
    print(f"{temparature} is hot")

else :
    print(f"{temparature} is damn hot")
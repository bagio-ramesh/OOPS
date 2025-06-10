num = int(input("Enter number: "))
for i in range(num,50+1):
    if i == 25:
        continue
    elif i == 50:
        break
    print(i,end=',')
lst = [-1,3,5,4,3,2,1]

clos = lst[0]

for num in lst:
    if abs(num) < abs(clos):
        clos = num

    elif clos < 0 and abs(clos) in lst:
        clos = abs(clos)

print("closest number is :",clos)

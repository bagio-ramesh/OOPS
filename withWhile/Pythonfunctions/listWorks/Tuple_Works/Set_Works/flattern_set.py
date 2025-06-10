arr = [ (1,10,3,4),(11,10,20,22,32),(1,20,44,32)]

new_set = set()

for lst in arr:
    for num in lst:
        new_set.add(num)

print(new_set)
arr = [1,2,3,4,5]

for i in range(1, len(arr) + 2):
    if i not in arr:
        missing_n = i
        break

print(missing_n) 
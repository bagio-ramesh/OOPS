arr = [
    (10,11,12),
    (4,5,6),
    (12,13,14)
]

new_lst = []

for tp in arr:
    for num in tp:
        new_lst.append(num)
print(sum(new_lst))

new_set = [num for tp in arr for num in tp]

print(sum(new_set))
arr=[
    [1,2,[10,20]],
    [2,20,[100,200,300]],
    [3,30,[100,200,300]],
    [4,40,[1]],
    [1000,2000]
]


# flatten arr
# display largest number
# dispaly smallest number
# total
new_lst = []
for num in arr:
    if isinstance(num, list):
        for sub_element in num:
            if isinstance(sub_element, list):
                new_lst.extend(sub_element)
            else:
                new_lst.append(sub_element)
    else:
        new_lst.append(num)

print(new_lst)

print(max(new_lst))

print(min(new_lst))

print(sum(new_lst))
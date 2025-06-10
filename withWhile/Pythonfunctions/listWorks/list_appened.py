arr = [10,64,34,46,46,23,22,8]

even_list = []

odd_list = []

for num in arr:
    if num % 2 == 0:
        even_list.append(num)
        
    else:
        odd_list.append(num)
        
print(even_list)

print(odd_list)

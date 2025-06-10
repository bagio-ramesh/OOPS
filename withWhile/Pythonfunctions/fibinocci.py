def fibinocci_se(n):
    current = 1
    pre = 0  
    for i in range(0, n + 1):
        next_num = pre + current
        pre = current
        current = next_num
    return next_num

num = int(input("Enter any Number: "))
result = fibinocci_se(num)
print(result)

def sum_of_nums(num):
    if num == 0:
        return 0
    
    return num+(sum_of_nums(num-1))

result = sum_of_nums(5)
print(result)
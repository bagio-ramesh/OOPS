def get_positive_nums(*nums):
    return[n for n in nums if n > 0]

result = get_positive_nums(-10,-2,3,4,-3,12,13)
print(result)



def neg_numbers(*nums):
    return [n for n in nums if n<0]
result1 = neg_numbers(-10,-2,3,4,-3,12,-34,13)
print(result1)


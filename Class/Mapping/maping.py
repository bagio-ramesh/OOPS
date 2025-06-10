from functools import reduce

num_lst = [5,10,25,30,35]

def cube(num):
    return num**3


cube_lst = list(map(cube,num_lst))
print(cube_lst)



add_lstt = list(map(lambda num:num+5,num_lst))
print(add_lstt)


even_nums = list(filter(lambda num:num%2==0,num_lst))
print(even_nums)


e_nums = [num for num in num_lst if num % 2 == 0]
print(e_nums)


tottal = reduce(lambda n1,n2:n1+n2,num_lst) 
print(tottal)

product = reduce(lambda n1,n2:n1*n2,num_lst)
print(product)

product = reduce(lambda n1,n2:n1*n2,num_lst)
print(product)



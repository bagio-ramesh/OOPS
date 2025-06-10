# def say_hai(n):
#     if n == 1:
#         return
#     print("Hai")

#     say_hai(n-1)

# #say_hai(6)


# # for loop iteration
# def Hello_py():
#     for i in range(1,6):
#         print("Hello Python")

# #Hello_py()


# # recursive method iteration
# def Hello_py(n):
#     if n == 1:
#         return
#     print("Hello Python")

#     Hello_py(n-1)

# #Hello_py(6)



# def display_my_name(n):
#     if n < 1:
#         return
#     print("Bagio")

#     display_my_name(n-1)

#display_my_name(4)


# def display_nums(limit):

#     if limit < 1:
#         return
    
#     print(limit)

#     display_nums(limit-1)

# display_nums(50)

def display_limit_sqrs(limit):
    if limit < 1:
        return
    print(limit**2)

    display_limit_sqrs(limit-1)

display_limit_sqrs(10)
def factorial_num(num):
    if num == 0 :
        return 1
    return num * factorial_num(num - 1)

print(factorial_num(1))
def fact_num(num):
    
    if num == 1:
        return 1
    else:
        return num*fact_num(num-1)
    
print(fact_num(5))
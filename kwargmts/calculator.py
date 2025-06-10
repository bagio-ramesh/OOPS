def calculator(*args,**kwargs):
    result = 1

    if kwargs.get("operand")== "+":
        return sum(args)
    
    elif kwargs.get("operand") == "-":
    
        for num in args:
            result= num - num
        return result
    
    elif kwargs.get("operand") == "*":
        
        for num in args:
            result=result*num

        return result


print(calculator(10,20,50,30,operand="+"))
print(calculator(50,20,operand="-"))
print(calculator(10,20,50,30,operand="*"))

def swap_dec(fn):
    def inner_fn(n1,n2):
        if n1 < n2:
            (n1,n2) = (n2,n1)

        return fn(n1,n2)
    
    return inner_fn


@swap_dec
def sub(n1,n2):
    return n1 - n2

@swap_dec
def div(n1,n2):
    return n1 / n2


print(sub(100,50))
print(div(100,50))



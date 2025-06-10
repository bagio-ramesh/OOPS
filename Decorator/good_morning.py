def add_good(fn):
    def inner_fn():
        return "Good" + fn()
    return inner_fn

@add_good
def say_morning():
    return "Morning"

@add_good
def say_evening():
    return "Evening"

@add_good
def say_night():
    return "Night"

print(say_morning())  
print(say_evening())  
print(say_night())  



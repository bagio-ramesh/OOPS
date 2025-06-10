from datetime import datetime

def add_greeting(fn):
    def inner_greeting(user):
        current_time = datetime.now().hour

        if current_time < 12:
            return fn(user) + " Good Morning"
        else:
            return fn(user) + " Good Afternoon"
        
    return inner_greeting






@add_greeting
def sent_greetings(user):
    return f"Hello {user}"


name = input("Enter any name asap!:")

print(sent_greetings(name))







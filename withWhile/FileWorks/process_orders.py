swiggy_path = "C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\swiggy.txt"

zomato_path = "C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\zomato.txt"

walkings_path = "C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\walkin_orders.txt"


order_count = {}

with open(swiggy_path,"r") as fr:
    for food in fr:
        item = food.rstrip("\n")

        order_count[item] = order_count.get(item,0)+1


with open(zomato_path,"r") as fr1:
    for food in fr1:
        item = food.rstrip("\n")

        order_count[item] = order_count.get(item,0)+1
       
with open(walkings_path,"r") as fr2:
    for food in fr2:
        item = food.rstrip("\n")

        order_count[item] = order_count.get(item,0)+1


print(order_count)

print(sorted(order_count,reverse=True,key=order_count.get))

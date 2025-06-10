branch1_stock = {"apple":3,"orange":3,"plum":5,"banana":10}
branch2_stock = {"apple":4,"orange":6,"plum":8}

current_stock = branch1_stock.copy()

for k in current_stock.keys():
    current_stock[k] = branch1_stock.get(k,0) + branch2_stock.get(k,0)

print(current_stock)

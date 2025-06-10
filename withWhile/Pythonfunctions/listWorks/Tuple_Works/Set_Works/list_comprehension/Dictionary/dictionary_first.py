# {} , key value pairs , duplicates not allowed , its a unique keys , picking keys by values!

shirt = {"shirtt":"lpshirt","price":2300,"brand":"Lp","material":"cotton"}

print(shirt["shirtt"])
print(shirt["price"])
print(shirt["brand"])
print(shirt["material"])

shirt["offer"]=399

print(shirt)

shirt["price"]+=2000
print(shirt)

shirt["brand"]="LP"
print(shirt)
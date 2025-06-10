mobiles = [
    {
        "code": "MB001",
        "title": "iPhone 15 Pro Max",
        "brand": "Apple",
        "price": 1199,
        "network": "5G"
    },
    {
        "code": "MB002",
        "title": "Galaxy S24 Ultra",
        "brand": "Samsung",
        "price": 1099,
        "network": "5G"
    },
    {
        "code": "MB003",
        "title": "Pixel 8 Pro",
        "brand": "Google",
        "price": 999,
        "network": "5G"
    },
    {
        "code": "MB004",
        "title": "OnePlus 12",
        "brand": "OnePlus",
        "price": 799,
        "network": "5G"
    },
    {
        "code": "MB005",
        "title": "Redmi Note 13 Pro",
        "brand": "Xiaomi",
        "price": 349,
        "network": "5G"
    },
    {
        "code": "MB006",
        "title": "Galaxy A54",
        "brand": "Samsung",
        "price": 449,
        "network": "5G"
    },
    {
        "code": "MB007",
        "title": "iPhone SE (2022)",
        "brand": "Apple",
        "price": 429,
        "network": "5G"
    },
    {
        "code": "MB008",
        "title": "Moto G Power 5G",
        "brand": "Motorola",
        "price": 299,
        "network": "5G"
    },
    {
        "code": "MB009",
        "title": "Nothing Phone (2)",
        "brand": "Nothing",
        "price": 599,
        "network": "5G"
    },
    {
        "code": "MB010",
        "title": "Realme GT Neo 5",
        "brand": "Realme",
        "price": 499,
        "network": "5G"
    }
]
# q1)total number of mobiles 
# q2)display all mobile names
# q3)display 5g mobiles names
# q4)mobile with price <$500

tottal_number_of_mobiles = len(mobiles)
print("Mobile Count =",tottal_number_of_mobiles)

all_mobiles_name = [mob.get("title") for mob in mobiles]
print("All Mobile Names=",all_mobiles_name)

f5G_mobiles_name = [mob.get("title") for mob in mobiles if mob["network"]== "5G"]
print("5g Mobiles=",f5G_mobiles_name)


mobile_under_500 = [mob.get("title") for mob in mobiles if mob["price"] < 500]
print("Mobiles Under $500=",mobile_under_500)
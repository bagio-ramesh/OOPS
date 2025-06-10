def get_value(**kwargs): # to get value by key using this function
    print(kwargs.get("salary"))

get_value(name="Bagio",place="Chalakudy",salary=300000)




def get_key_value(**kwargs):  # to separate key value pairs on this function
    for k,v in kwargs.items():
        print(k,v)

get_key_value(name ="Bagio",batch="Python",Place="Chalakudy")



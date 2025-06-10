class Product:

    def __init__(self,code,title,price,category): # Constructor and initilizing instance Variables,Its autyomatically invokes during creation

        self.code = code

        self.title = title

        self.price = price

        self.category = category

    def display_product(self):
        print(self.code,self.title,self.price,self.category)

    def __str__(self):   # Object srting Representation
        return self.title
    

pro_instance1 = Product(762367,"PHONE",30000,"MObile")

pro_instance2 = Product(76365,"Car",5655777,"Vehicle")

print(pro_instance1)
print(pro_instance2)
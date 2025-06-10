class Cart:
    def __init__(self,user):
        self.user = user
        self.basket = []
    
    def add_to_basket(self,**kwargs):

        self.basket.append(kwargs)

        print("The item has been added to cart")

    def remove_basket_item(self,id):

        for rb in self.basket:
            if rb.get("id") == id:
                self.basket.remove(rb)

    def cart_summary(self):

        for cm in self.basket:
    
            print(f"Id = {cm.get('id')} title = {cm.get('title')} price = {cm.get('price')} qty = {cm.get('qty')} Tottal = {cm.get('price')*cm.get('qty')}")
            basket_tottal = sum([cm.get("qty")*cm.get("price") for cm in self.basket])
        print(f"Tottal Basket cost: {basket_tottal}")



cart_instance1=Cart("bagio")

cart_instance1.add_to_basket(id=1,title ="samsung A51",price = 87676, qty=1)

cart_instance1.add_to_basket(id=2,title ="Iphone 4",price = 47000, qty=2)

cart_instance1.add_to_basket(id=3,title ="Iphone 15",price = 10000, qty=1)

print(cart_instance1.basket)

cart_instance1.remove_basket_item(1)

print(cart_instance1.basket)

cart_instance1.cart_summary()

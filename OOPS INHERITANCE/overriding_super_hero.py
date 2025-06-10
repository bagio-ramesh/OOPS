class Superhero:

    def __init__(self,name):
        self.name = name

    def super_powers(self):
        print("Super Power")

class Spiderman(Superhero):

    def __init__(self, name):
        super().__init__(name)

    def super_powers(self):
        print(self.name,"Speed,Jump and reflex")

class Batman(Superhero):

    def __init__(self, name):
        super().__init__(name)

    def super_powers(self):
        print(self.name,"Money")

Spiderman_instance = Spiderman("Bagio")
Spiderman_instance.super_powers()

batman_instance = Batman("Bagio")
batman_instance.super_powers()


    
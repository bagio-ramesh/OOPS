class FPlayers:
    def set_fplyayers(self,name,position,team,salary):

        self.name = name

        self.position = position

        self.team = team

        self.salary = salary

    def display_fplayers(self):
        print(self.name,self.position,self.team,self.salary)

player_instance1 = FPlayers()

player_instance1.set_fplyayers("Messi","Right Forward","Inter Miami",300000)

player_instance1.display_fplayers()

    

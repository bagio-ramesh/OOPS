import copy

manu_fav_food = [["Coffee","Chapati"],["Meals"],["Meals"]]

bagis_fav_food = copy.deepcopy(manu_fav_food)

bagis_fav_food[0][0] = "Juice"

print(manu_fav_food)
print(bagis_fav_food)
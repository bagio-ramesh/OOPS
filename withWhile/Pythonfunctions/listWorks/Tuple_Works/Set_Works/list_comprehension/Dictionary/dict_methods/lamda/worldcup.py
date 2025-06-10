world_cup_winners = {
    "Australia": 6,   
    "India": 2,      
    "West Indies": 2,
    "Pakistan": 1,    
    "Sri Lanka": 1,   
    "England": 1,     
}

# team with most number wins

# team with least number of wins

# total number of world cups


def key_value(key):
    return world_cup_winners.get(key)

max_wins = max(world_cup_winners,key=key_value)
print(max_wins,world_cup_winners.get(max_wins))

min_wins = min(world_cup_winners,key=key_value)

least_count = world_cup_winners.get(min_wins)

for k,v in world_cup_winners.item():
    if v == least_count:
        print(k,v)

tottal = [tot for tot in world_cup_winners.values()]
print(sum(tottal))




character_lst = ["A","I","V","I","L","C","D","D","F","X","B","V","M"]

romans = "IVLVCDM"

new_dict = {}

for w in romans:
    if w in character_lst:
        new_dict[w] = character_lst.count(w)

print(new_dict)
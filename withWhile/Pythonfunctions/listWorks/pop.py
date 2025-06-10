colors = ["blue","blue","yellow","black","green","green","green"]

removed_item = colors.pop(0)
print(removed_item)


colors.remove("blue")
print(colors)

yellow_index = colors.index("yellow")
print(yellow_index)


count = colors.count("green")
print(count)



colors.reverse()
print(colors)
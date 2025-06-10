tp = (1,23,45,45,76,89)

print(tp) # duplicate allowed

first_element = tp[0]
print(first_element)

#add_elememt = tp[1]= 200
#print(add_elememt)  # its immutable cant replace it!


pos = tp.index(23)
print(pos)

freq = tp.count(45)
print(freq)
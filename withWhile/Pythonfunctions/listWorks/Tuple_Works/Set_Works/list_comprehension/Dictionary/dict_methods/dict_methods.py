alpha = {"A":"abhi","B":"Bagi","C":"caba"}

for w in alpha.keys():
    print(w) # keys pick

for v in alpha.values():
    print(v) # values pick


for k,v in alpha.items():
    print(k,"=",v)  #  key value pairs pick

print(alpha.get("a","NoNo"))
print("Exit")  # pick key with value only onece with argument

deel = alpha.pop("C")
print(deel) # for del the key value pairs in the dict!
print(alpha)


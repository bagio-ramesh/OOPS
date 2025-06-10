arr = [100,200,300,400,500]
k=2

for i in range(0,k):
    last_element = arr.pop()
    arr.insert(0,last_element)
print(arr)

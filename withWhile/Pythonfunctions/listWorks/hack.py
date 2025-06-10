x = int(input("Enter any four numbers:; "))
y = int(input())
z = int(input())
n = int(input())

result = []

for i in range (x + 1):
    for k in range (y + 1):
        for m in range (z + 1):
            if i + k + m != n:
                result.append([i,k,m])
print(result)


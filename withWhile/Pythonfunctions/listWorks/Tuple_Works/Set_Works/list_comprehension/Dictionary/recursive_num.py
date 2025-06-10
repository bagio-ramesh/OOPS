words = "ABCAB"

wc = {}

for w in words:
    if w not in wc:
        wc[w]=1

    else:
        print(w,"is the recursiuve character")
        break


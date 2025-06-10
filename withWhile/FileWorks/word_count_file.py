f = open("C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\word_count.txt","r")

new_dics = {}

for line in f:
    words = line.split()

    for w in words:
        if w in new_dics:
            new_dics[w]+=1

        else:
            new_dics[w]=1

print(new_dics)
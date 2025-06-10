f = open("C:\\Users\\hp\\OneDrive\\Desktop\\pythonworks\\withWhile\\FileWorks\\new.txt","r")

news_lst = []

for line in f:
    words = line.split()

    for w in words:
        news_lst.append(w)

print(news_lst)
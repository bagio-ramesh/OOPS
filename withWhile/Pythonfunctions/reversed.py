word = input("Enter a word: ")

len_word = len(word)-1

for i in range(len_word,-1,-1):
    print(word[i],end="")
    
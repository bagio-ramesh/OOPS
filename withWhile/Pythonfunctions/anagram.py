word = "silent".lower()
word1 = "listen".lower()

word_first = sorted(word)

word_sec = sorted(word1)

if word_first == word_sec:
    print("Anagram")

else:
    print("Its not!")
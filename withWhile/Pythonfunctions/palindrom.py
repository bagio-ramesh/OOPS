word = input("Enter a word: ")

sliced_word = word[::-1]

if word == sliced_word:
    print("Palindrom")

else:
    print("Its not")
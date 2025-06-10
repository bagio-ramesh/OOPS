word = "the five boxing wizards jump quickly"
alphabets = "abcdefghijklmnopqrstuvwzyx"
is_pangram = True

for ch in alphabets:
    if ch not in word:
        is_pangram = False
print(is_pangram)
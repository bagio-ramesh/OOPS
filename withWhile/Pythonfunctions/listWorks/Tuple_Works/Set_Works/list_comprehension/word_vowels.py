words = ["python","django","oodo","Imma"]

VOWELS = "aeiouAEIOU"

vowel_words = [ w for w in words if w[0] in VOWELS]

print(vowel_words)
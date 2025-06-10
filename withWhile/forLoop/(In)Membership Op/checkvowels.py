word = "Bagio Ramesh"
VOWELS = "aeiou"
v_count = 0

for ch in VOWELS: #ch=b
    if ch in word:
        v_count+=1
print(f"Vowel:{v_count}")
print(len(word))

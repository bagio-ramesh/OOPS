word = "pneumonoultramicroscopicsilicovolcanoconiosis"
VOWELS = "aeiou"
v_count = 0
c_count = 0

for ch in word:
    if ch in VOWELS:
        v_count+=1

    elif ch not in VOWELS:
        c_count+=1
print(f"Vowels:{v_count}")
print(f"Consonants:{c_count}")
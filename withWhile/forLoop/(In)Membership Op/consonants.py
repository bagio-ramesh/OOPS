word = "Sugumaran"
vowels = "aeiou"
c_count = 0

for ch in word:
    if ch not in vowels:
        c_count+=1
print(f"consonant:{c_count}")
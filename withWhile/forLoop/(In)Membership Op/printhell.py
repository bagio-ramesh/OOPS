text = "hello world python"
VOWELS = "aeiou"
v_count =  0

for ch in text:
    if ch in VOWELS:
        v_count+=1

    if v_count == 2:
        break
    print(ch)
text = "india won by 10 wickets with 20 overs remaining"
count = 0

for ch in text:
    if ch.isdigit():
        count+=1

print(count)
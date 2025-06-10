#osi = "01234567"
text = "bagiobag"
search_word = "bag"
freq = 0
len_text_word = len(text)
len_srch_word = len(search_word)

limit = len_text_word - len_srch_word

for i in range(0,limit+1):
    sliced_word = text[i:i+len_srch_word]
    if sliced_word == search_word:
        freq+=1

print(freq)


#i = 0

#sliced_word = text[0:3] = "bag"

#"bag" == "bag" → freq = 1

#i = 1

#sliced_word = text[1:4] = "agi"

#"agi" != "bag" → No change.

#i = 2

#sliced_word = text[2:5] = "gio"

#"gio" != "bag" → No change.

#i = 3

#sliced_word = text[3:6] = "iob"

#"iob" != "bag" → No change.

#i = 4

#sliced_word = text[4:7] = "oba"

#"oba" != "bag" → No change.

#i = 5

#sliced_word = text[5:8] = "bag"

#"bag" == "bag" → freq = 2
def string_reverse(word):
    if len(word) <= 0:  
        return word
    return string_reverse(word[1:]) + word[0]

print(string_reverse("Sandra")) 
print(string_reverse("Bagio")) 


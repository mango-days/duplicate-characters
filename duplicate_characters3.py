s = "abcabcdefgabc"
library = ""
for key in s :
    if key not in library : library += key
    else : print ( key )

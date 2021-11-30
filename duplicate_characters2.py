s = "abcabcdefgabc"
library = {}
for key in s :
    if key not in library : library [ key ] = 1
    else : 
        library [ key ] += 1
        print ( key )

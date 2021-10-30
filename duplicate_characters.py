str="abcabcdefgabc"
dict={}
for x in str:
    if x in dict.keys(): dict[x]+=1
    else: dict[x]=1
for x, y in dict.items():
    if y>1: print(x,y)

str="abcabcdefgabc"
check="" # set of unique characters
size=len(str)
index=1
check+=str[0]
while index<size :
    temp=str[index]
    check_index=0
    flag=0
    while check_index<len(check):
        if temp==check[check_index]:
            print(temp)
            flag=1
            break
        check_index+=1
    if flag==0: check+=temp
    index+=1
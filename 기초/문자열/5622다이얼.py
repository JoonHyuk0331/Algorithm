string=input()
result=0
setlist=[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
for c in string:
    result+=(setlist[ord(c)-65]+1)
print(result)
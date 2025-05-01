str1=input()
list=[-1]*26
i=0
for c in str1:
    #list.insert(ord(c)-97,i) 틀린코드
    if(list[ord(c)-97]==-1):
        list[ord(c)-97]=i
    i+=1
for i in list:
    print(i,end=" ")
    
## -1로 초기화된 배열 만들기 [-1]*26

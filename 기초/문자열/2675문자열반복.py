n=int(input())
for i in range (n):
    l,str=input().split(" ")
    for c in str :
        print(c*int(l),end='') #end=''는 붙이기기
    print()
        

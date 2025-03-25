n,m=map(int,input().split(' '))
list=[i+1 for i in range(n)]
    
for i in range (m):
    a,b=map(int,input().split(' '))
    list[a-1:b]=list[a-1:b][::-1]
    
for i in list:
    print(i,end=' ')
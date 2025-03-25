n,m=map(int,input().split(' '))
list=[]
for i in range (n):
    list.append(i+1)
    
for i in range (m):
    a,b=map(int,input().split(' '))
    temp=list[a-1]
    list[a-1]=list[b-1]
    list[b-1]=temp
    
for i in list:
    print(i,end=' ')
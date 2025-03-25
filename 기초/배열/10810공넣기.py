n,m=map(int,input().split(' '))
list=[0]*n

for l in range (m):
    i,j,k=map(int,input().split(' '))
    for p in range (i,j+1) :
        list[p-1]=k
        
for i in list :
    print(i,end=" ")
n,m,k=map(int,input().split(' '))
data=list(map(int,input().split(' ')))

data.sort(reverse=True)
first=data[0]
second=data[1]
result=0

rotate=0
for i in range(m):
    if(rotate>=k):#k번 반복했다면
        rotate=0#초기화
        result+=second
        continue
        
    result+=first
    rotate+=1
        
print(result)
        
a,b,c=map(int,input().split(' '))
result=0
#3개 다 같을때

if a==b and b==c :
    result=10000+a*1000
elif a==b or a==c :
    result=1000+a*100
elif b==c :
    result=1000+b*100
else :
    result=max(a,b,c)*100
    
print(result)
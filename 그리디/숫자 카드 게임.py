n,m=map(int,input().split(' '))

select_list=[]
for i in range (n):
    list=(map(int,input().split(' ')))
    select_list.append(min(list))
print(max(select_list))
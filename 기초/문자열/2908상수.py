list=input().split()
a=len(list)
for i in range(a):
    list[i]=int(list[i][::-1])

print(max(list))
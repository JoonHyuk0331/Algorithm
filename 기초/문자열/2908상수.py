list=input().split()
a=len(list)
for i in range(a):
    list[i]=int(list[i][::-1])

print(max(list))

#step에 음수를 주면 문자열을 거꾸로 읽을 수 있다.
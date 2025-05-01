list=[0]
n=int(input())
for i in range (2000000000):
    if list[-1] > n: #끝자리가 합이면
        print(i-2)
        break
    list.append(list[-1]+i)

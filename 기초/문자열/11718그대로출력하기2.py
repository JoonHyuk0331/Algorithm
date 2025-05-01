num = input()
numbers = list(map(int,input()))

print(sum(numbers))

#map(int,input()) 이 가능한 이유
#input은 str 형으로 받아오기 때문에 54321이 오더라도 '54321'이 아닌 list[5,4,3,2,1]로 받아짐짐
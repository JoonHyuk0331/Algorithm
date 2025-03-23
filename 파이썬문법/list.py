#리스트 선언
a=[1,2,3,4]
b=list()

#크기가 n이고 모든값이 0인 1차원 리스트
n=10
arr=[0]*n
print(a)

#인덱싱 슬라이싱
print(a[-1])
print(a[1:3])

#리스트 컴프리헨션 ->한줄로 리스트 초기화
array=[i for i in range(20) if i % 2 == 1]
#동일하다
array=[]
for i in range(20):
    if i % 2 ==1:
        array.append(i)
#1부터 9까지 수의 제곱 값을 포함하는 리스트
array=[i*i for i in range(1,10)]
#이차원 리스트 초기화하기 NxM 크기의 2차원 리스트 초기화
n=3
m=4
array=[[0]*m for _ in range(n)]
#언더바는 반복시 반복변수값 무시를 위해 사용용
print(array)

#append가 insert보다 빠르다

#특정한 원소 제거
a=[1,2,3,4,5,5,5]
remove_set={3,5}

#remove_set에 포함되지 않은 값만을 저장
result=[i for i in a if i not in remove_set]
print(result)
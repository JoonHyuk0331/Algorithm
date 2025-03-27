#아주 큰 수(INF)
print(1e9)

#실수형 처리
a=0.3+0.6
print(a)
a=round(a,4)
print(a)

#나누기,나머지,몫
a=7
b=3
print(a/b)
print(a//b)

#거듭제곱 연산자 x^y
print(3 ** 2)

help(print)


#튜플 자료형
#소괄호를 이용해 초기화
a=(1,2,3,4)
#한 번 선언된 값을 변경할 수 없다. -> 최단경로 알고리즘 우선순위 큐 구성시 사용

#딕셔너리 자료형 -> 키 값 쌍으로 이루어진 데이터 처리시 리스트보다 빠름
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
data=dict()
data['사과']='Apple'
data['바나나']='Banana'

#딕셔너리에 특정 자료 존재유무?
if '사과' in data:
    print("사과를 키로 가지는 데이터가 존재합니다")
    
#키와 데이터만 따로 뽑을수도 있다


#집합 자료형, 특정한 데이터가 이미 등장한 적 있는지 여부 체크시 효과적
data1=set([1,2,3])
data2={1,2,3}
#둘이동일
#집합의 연산
print(data1|data2)#합집합
print(data1&data2)#교집합
print(data1-data2)#차집합

#add나 remove 사용가능

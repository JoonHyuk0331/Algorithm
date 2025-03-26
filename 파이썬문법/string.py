#문자열 초기화
#큰따옴표나 작은따옴표 이용
a="hello"

#멀티라인 따옴표 3개로 감싸면 \n 필요없음
a="""hi
my
name
is
jun"""

#문자 여러번 출력
print(a*3)

#문자열도 리스트로 슬라이싱 가능 2는 포함 3은 포함x
print(a[2:3])

#문자열 중간 바꾸기
a = "Pithon"
a[:1]
'P'
a[2:]
'thon'
a[:1] + 'y' + a[2:]
'Python'

#문자열 포맷팅1
number=3
str1="I eat %d apples." % number
food="apple"
str2="I eat %d %ss" % (number,food)

print(str2)

#정렬과 공백
str3="%10s" % "hi"
print(str3)

#소수점 표현
str4="%0.4f" % 3.42134234
print(str4)

#format 함수를 사용한 포매팅
str5="I eat {0} {1}s".format(number,food)
str6="I eat {number} {food}s".format(number=3,food="apple")

#f문자열 포맷팅
name = '홍길동'
age = 30
str7=f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

d = {'name':'홍길동', 'age':30}
str8=f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

#문자열 관련 함수들 ***주의 문자열은 immutable 변수라 문자열 함수 사용시 문자열 자체가 바뀌는게 아니라 바뀐 복사본을 리턴함함
#문자 개수 세기 - count
a = "hobby"
a.count('b') #2

#위치 알려 주기 1 - find
a = "Python is the best choice"
a.find('b')#14
a.find('k')#-1 (존재하지 않음)

#위치 알려 주기 2 - index
a = "Life is too short"
a.index('t') #8

#문자열 사이에 삽입 - join
",".join('abcd')
'a,b,c,d'

#대문자,소문자 변환
a.upper
a.lower

#공백지우기
a.lstrip
a.rstrip
a.strip

#문자열 변경경
a = "Life is too short"
a.replace("Life", "Your leg")

#문자열 나누기 - 공백
a = "Life is too short"
a.split()
['Life', 'is', 'too', 'short']

#문자열 나누기
b = "a:b:c:d"
b.split(':')
['a', 'b', 'c', 'd']

#TMI
#왼쪽정렬
str="{0:<10}".format("hi")
#가운데정렬
str="{0:^10}".format("hi")
#공백채우기
str="{0:=^10}".format("hi")
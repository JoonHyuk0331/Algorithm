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

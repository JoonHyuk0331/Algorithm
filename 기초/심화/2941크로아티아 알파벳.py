sss=input()
result=0
calphalsit=['c=','c-','dz=','d-','lj','nj','s=','z=']
#크로아티아 알파벳 개수 세기기
for i in calphalsit:
    #print(f'{i}에 대한 검사를 실시합니다---')
    while sss.find(i) != -1:#타겟 문자가 찾아지지 않을때까지
        pos=sss.find(i)
        #print(f'위치:{pos}에서 {i}가 발견되었습니다')
        sss=sss[:pos]+':'+sss[pos+len(i):]
        #print(f'슬라이싱하고 남은 문자열: {sss}')
        result+=1
    #print(f'{i}에 대한 검사를 종료합니다---')
    
#print('크로아티아 알파벳 제외한 결과과'+sss)
sss=sss.replace(':','')
#print(':를 제거한 결과'+sss)
result+=len(sss)
#print(f'나머지 일반 알파벳의 개수만큼 더했습니다{len(sss)}')

print(result)

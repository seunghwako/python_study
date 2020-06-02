a = 1
b = 2
temp = 2 # 결과값 임시 저장 변수
sum = 2 # 2도 짝수이므로 더해줘야해서 2로 고정

limit = 4000000 # 4000000 이하로 제한

while a <= 4000000:
    a = a+b # 피보나치 수열 계산
    b = temp # 이전의 값 임시 저장
    temp = a # 이전 결과 값 임시 저장

    if a%2 == 0: # 짝수 일때만 고려
        sum = sum + a

print(sum)
    
    


    
    









    


    





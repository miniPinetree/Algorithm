## 접근방식
# w(a,b,c) 재귀함수를 매번 계산해야 하므로 오랜 시간이 걸린다. 
# 결과 값들을 메모이제이션하여 중복 연산은 방지한다.

## 유의사항
# 문제에서 주어진 재귀함수는 파이썬 문법이 아니므로 해당 식을 코드에 삽입하려면 변환해야 한다.

import sys

def w(a, b, c):
    #이미 계산된 결과가 존재하는 지 판단
    if (a,b,c) in memo.keys():
        return memo[(a,b,c)]

    # 계산된 결과가 존재하지 않는다면 
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)

    elif a < b < c:
        memo[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[(a,b,c)]
    else:
        memo[(a,b,c)]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memo[(a,b,c)]
    
while True:
    a,b,c = map(int,sys.stdin.readline().split())
    
    # 재귀함수 탈출 조건
    if (a,b,c) == (-1,-1,-1):
        break

    memo = dict()
    print(f'w({a},{b},{c}) = {w(a,b,c)}')
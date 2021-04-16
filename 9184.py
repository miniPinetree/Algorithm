<<<<<<< HEAD
## 접근방식
# w(a,b,c) 재귀함수를 매번 계산해야 하므로 오랜 시간이 걸린다. 
# 결과 값들을 메모이제이션하여 중복 연산은 방지한다.

## 유의사항
# 문제에서 주어진 재귀함수는 파이썬 문법이 아니므로 해당 식을 코드에 삽입하려면 변환해야 한다.

import sys

memo = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    # 큰 숫자가 입력되어도 20으로 조정하기 위해 먼저 판단한다.
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)


    #이미 계산된 결과가 존재하는 지 판단
    if memo[a][b][c]:
        print(memo[a][b][c])
        return memo[a][b][c]

    #저장된 결과가 없다면 재귀함수로 계산한 결과를 저장
    if a < b < c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        memo[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    print(memo[a][b][c])
    return memo[a][b][c]
    
while True:
    a,b,c = map(int,sys.stdin.readline().split())
    
    # 재귀함수 탈출 조건
    if (a,b,c) == (-1,-1,-1):
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))
=======
## 접근방식
# w(a,b,c) 재귀함수를 매번 계산해야 하므로 오랜 시간이 걸린다. 
# 결과 값들을 메모이제이션하여 중복 연산은 방지한다.

## 유의사항
# 문제에서 주어진 재귀함수는 파이썬 문법이 아니므로 해당 식을 코드에 삽입하려면 변환해야 한다.

import sys

memo = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    # 큰 숫자가 입력되어도 20으로 조정하기 위해 먼저 판단한다.
    elif a > 20 or b > 20 or c > 20:
        return w(20,20,20)


    #이미 계산된 결과가 존재하는 지 판단
    if memo[a][b][c]:
        print(memo[a][b][c])
        return memo[a][b][c]

    #저장된 결과가 없다면 재귀함수로 계산한 결과를 저장
    if a < b < c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        memo[a][b][c]=w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    print(memo[a][b][c])
    return memo[a][b][c]
    
while True:
    a,b,c = map(int,sys.stdin.readline().split())
    
    # 재귀함수 탈출 조건
    if (a,b,c) == (-1,-1,-1):
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))
>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095

# 문제 : 가지고 있는 N종류의 동전을 가지고 K가치를 만드는데 필요한 동전 개수의 최솟값
# 접근방식 :
# 1. 문제 조건에 따르면 주어진 동전의 종류는 모두 배수이고 항상 1을 포함한다.
# 2. 선택지가 모두 배수인 경우 무조건 큰 값부터 처리해도 최적의 해를 구할 수 있다.
# 3. 즉 그리디 알고리즘을 사용해도 되는 문제에 해당한다.
# 코드구현
# 1. 입력받는 N개의 동전 가치를 리스트로 저장한다. (오름차순이므로 정렬과정 불필요)
# 2. 리스트의 뒤에 있는 값부터 k를 나눠간다.

import sys

r = sys.stdin.readline

n, k = map(int, r().split())
coin_list= []
for _ in range(n):
    coin = int(r())
    coin_list.append(coin)

cnt = 0
for coin in reversed(coin_list):
    if k==0:
        break
    elif k>=coin: #오답 포인트 : 서로 값이 같은 경우도 나눗셈이 가능함에 유의하자.
        cnt += k//coin
        k = k%coin

print(cnt)


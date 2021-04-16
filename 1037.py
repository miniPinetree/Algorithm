# 문제
# 진짜 약수의 조건 : 약수가 1과 N이 아니어야 한다. 
# 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구해야한다.
# 접근방식 : x의 약수를 크기순으로 정렬했을 때 x의 제곱근을 기준으로 대칭하여 서로 곱하면 x가 된다.
# 코드구현 : 약수가 정렬 상태라면 양 끝의 위치한 약수(서로 대칭)를 곱하면 된다.
# 오답포인트 : 약수가 크기 순서대로 입력된다는 말이 없다!! 그러므로 정렬을 거쳐야한다.
n = int(input())
divisors = sorted(list(map(int, input().split())))
print(divisors[0]*divisors[-1])
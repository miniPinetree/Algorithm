### 1번 풀이 
# 팩토리얼 (이항계수의 정의 첨부) 
n,k = map(int,input().split())

def factorial(n):
    ans = 1 # 기본값을 1로 두어야 0!일 때 1이 출력된다.
    for i in range(2, n+1):
        ans *= i
    return ans

def Binomial(n,k):
    return factorial(n)//factorial(k)//factorial(n-k)

print(Binomial(n,k))


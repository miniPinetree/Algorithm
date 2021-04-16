def factorial(n):
    ans = 1 # 기본값을 1로 두어야 0!일 때 1이 출력된다.
    for i in range(2, n+1): #0과 1을 제외한 수부터
        ans *= i
    return ans

def Binomial(n,k):
    return factorial(n)//factorial(k)//factorial(n-k)

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    print(Binomial(m,n))
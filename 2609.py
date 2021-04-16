x,y = map(int, input().split())


 # 헐 뭘로 먼저 나누든 .. 알아서 큰값/작은값으로 조정된다..고로 비교는 필요없다.
 # x, y = max(x,y),min(x,y)     
r = x%y # 큰 수를 작은 수로 나누어준다.

# 유클리드 호제법
def gcd(x,y):
    r = x%y
    while r:
        x = y
        y = r
        r = x%y
    return y

print(gcd(x,y)) #최대공약수
print(x*y//gcd(x,y)) #최소공배수
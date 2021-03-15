
def gcd(a,b):
    r = a%b
    while r:
        a = b
        b = r
        r = a%b
    return b

t = int(input())
rst = []
for _ in range(t):
    a, b = map(int,input().split())
    rst.append(a*b//gcd(a,b))

for r in rst:
    print(r)





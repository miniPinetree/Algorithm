<<<<<<< HEAD
n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp=[0 for _ in range(n)]

dp[0] = stairs[0]

#1~3번째 계단은 점화식이 적용되지 않는다.
for i in range(1,n):
    if i<=2:
        dp[i] = max(stairs[i-1]+stairs[i],dp[0]+stairs[i])
    else:
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

=======
n = int(input())
stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp=[0 for _ in range(n)]

dp[0] = stairs[0]

#1~3번째 계단은 점화식이 적용되지 않는다.
for i in range(1,n):
    if i<=2:
        dp[i] = max(stairs[i-1]+stairs[i],dp[0]+stairs[i])
    else:
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
print(dp[n-2]) #n이 저장된 인덱스 값
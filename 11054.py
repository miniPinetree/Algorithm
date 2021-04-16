n = int(input())
nums = list(map(int,input().split()))
arr = [1]*n #부분수열의 길이를 저장
arr2 = [1]*n #역방향일 때 수열 길이를 저장한다.

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            arr[i] = max(arr[i],arr[j]+1) #dp방식

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if nums[i] > nums[j]:
            arr2[i] = max(arr2[i], arr2[j]+1)
max_rst=0
for i in range(n): #증가수열 길이, 감소수열 길이의 합이 가장 길어지는 지점을 찾는 과정
    if arr[i]+arr2[i] > max_rst:
        max_rst = arr[i]+arr2[i]
print(max_rst-1) #증가수열과 감소수열은 수열의 i번째 수를 공유하므로 이중합산된 개수에서 1을 차감한다.
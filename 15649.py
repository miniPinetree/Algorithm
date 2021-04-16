import sys
r = sys.stdin.readline
n,m = map(int,r().split())
arr = [0]*m
is_used = [0]*(n+1) 

def dfs(arr_idx):
    if arr_idx == m:#탈출조건
        print(*arr) #수열 길이 충족 시 현재까지 저장된 수열 출력
        return
    for i in range(1,n+1):
        if not is_used[i]: #숫자 사용여부 판단
            is_used[i] = 1
            arr[arr_idx]=i
            dfs(arr_idx+1)
            is_used[i]=0
        
dfs(0)
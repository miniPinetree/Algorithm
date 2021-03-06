<<<<<<< HEAD
### 접근방식
# 모든 경우의 수를 다 탐색해야 하는 경우이므로 DFS
# DFS + 가지치기 = 백트랙킹

### 설계과정
# DFS에 필요한 것
# 1. 연결관계를 알 수 있는 배열(이 문제에는 1부터 N까지 자연수 중 수열을 고르는 것으로 특정한 연결관계가 없어 필요치않다.)
# 2. 방문여부를 체크하는 배열(이 문제에서는 기 사용된 숫자를 체크하여 수열 내에 숫자가 중복되지 않도록 하는 역할을 한다.)
# 
n,m = map(int,input().split())
arr = [0]*m #탐색한 수열을 저장할 곳
visited=[0]*(n+1) #인덱스 1부터 사용하기 위해 n+1길이로 생성 

def dfs(arr_idx, start_num):
    if arr_idx == m: #탈출조건
        print(*arr)  #수열 길이 충족 시 현재까지 저장된 수열 출력
        return

    # 방문하지 않은 노드라면 재귀적으로 방문해 감.
    for i in range(start_num,n+1):#반복 범위를 함수인자로 두어 반복 최소화
        if not visited[i]:
            visited[i]=1
            arr[arr_idx]=i
            dfs(arr_idx+1,i+1) #수열의 다음 순서로 i보다 작은 수는 올 수 없다.
            visited[i]=0 #재귀함수에서 나왔다는 것은 탈출조건에 해당되어 수열의 출력까지 마쳤다는 것
            #공통으로 사용되는 visited[i] 리스트를 초기화시킨다.

=======
### 접근방식
# 모든 경우의 수를 다 탐색해야 하는 경우이므로 DFS
# DFS + 가지치기 = 백트랙킹

### 설계과정
# DFS에 필요한 것
# 1. 연결관계를 알 수 있는 배열(이 문제에는 1부터 N까지 자연수 중 수열을 고르는 것으로 특정한 연결관계가 없어 필요치않다.)
# 2. 방문여부를 체크하는 배열(이 문제에서는 기 사용된 숫자를 체크하여 수열 내에 숫자가 중복되지 않도록 하는 역할을 한다.)
# 
n,m = map(int,input().split())
arr = [0]*m #탐색한 수열을 저장할 곳
visited=[0]*(n+1) #인덱스 1부터 사용하기 위해 n+1길이로 생성 

def dfs(arr_idx, start_num):
    if arr_idx == m: #탈출조건
        print(*arr)  #수열 길이 충족 시 현재까지 저장된 수열 출력
        return

    # 방문하지 않은 노드라면 재귀적으로 방문해 감.
    for i in range(start_num,n+1):#반복 범위를 함수인자로 두어 반복 최소화
        if not visited[i]:
            visited[i]=1
            arr[arr_idx]=i
            dfs(arr_idx+1,i+1) #수열의 다음 순서로 i보다 작은 수는 올 수 없다.
            visited[i]=0 #재귀함수에서 나왔다는 것은 탈출조건에 해당되어 수열의 출력까지 마쳤다는 것
            #공통으로 사용되는 visited[i] 리스트를 초기화시킨다.

>>>>>>> 88d5abf5fdf1224584809c4f7ffbcfc6b01b5095
dfs(0,1)
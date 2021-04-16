### 문제요약
# DFS와 BFS로 구현하고 방문한 순서를 출력
### 접근방식
# 정점의 개수가 1,000개 이하이고 시간복잡도를 우선시하기 위해 2차원 배열을 만들 것이다.
# DFS는 스택, BFS는 큐를 이용한다.
# 정점 번호와 인덱스 일치를 위해 인덱스0은 비워둘 것이다.

### 설계과정
# 2차원 배열을 통해 연결 과정을 구현하려할 때 N*N으로 작성하면 됨.
# 1,2가 주어졌을 때 graph[1][2]에는 저장되지만 graph[2][1]에는 어떻게 저장시킬 지 고민함.
# 아주 간단한 코드로 가능한 문제임에도 복잡하게 생각했다 하하.

import sys
from collections import deque

### DFS방식
def dfs(graph,v,visited):
    # 현재 노드를 방문처리
    visited[v]=True
    print(v, end=' ')
    # 연결 노드 중 방문하지 않은 노드라면 재귀적으로 방문해 감.
    for i in range(1,n+1):
        if not visited[i] and graph[v][i]==1:
            dfs(graph,i,visited)

### BFS방식
def bfs(graph,v,visited):
    queue = deque([v])
    # 현재 노드를 방문처리
    visited[v]=True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접노드 추가
        for i in range(1,n+1):
            if not visited[i] and graph[v][i]==1:
                queue.append(i)
                visited[i] = True

r=sys.stdin.readline
n,m,v = map(int, r().split())
visited = [False]*(n+1)
graph =[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,r().split())
    graph[x][y]=graph[y][x]=1

dfs(graph,v,visited)
visited=[False]*(n+1)
print()
bfs(graph,v,visited)



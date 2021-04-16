
import sys 

read = sys.stdin.readline

graph={}
for i in range(int(read())):
    graph[i+1] = set()

for j in range(int(read())):
    a, b = map(int, read().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited=[]

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for adjacent_node in adj_graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)
    return visited

# print(bfs_queue(graph,1))
print(len(set(bfs_queue(graph,1)))-1)
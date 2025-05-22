from collections import deque

# DFS 함수
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 함수
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 입력 처리
n, m, start = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 처리 리스트 초기화
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

# DFS와 BFS 실행
dfs(graph, start, visited_dfs)
print()
bfs(graph, start, visited_bfs)

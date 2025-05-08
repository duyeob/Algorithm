import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 늘려서 깊은 재귀 호출도 처리 가능하도록 설정

def dfs(node, visited, graph):
    visited[node] = True  # 현재 노드를 방문 처리
    for neighbor in graph[node]:  # 현재 노드와 연결된 모든 이웃 노드 탐색
        if not visited[neighbor]:  # 이웃 노드가 아직 방문되지 않았다면
            dfs(neighbor, visited, graph)  # 재귀적으로 DFS 호출

# 입력 받기
N, M = map(int, input().split())  # N: 노드 수, M: 간선 수
graph = [[] for _ in range(N + 1)]  # 그래프를 인접 리스트 형태로 초기화 (1번 노드부터 사용)

for _ in range(M):  # M개의 간선 정보 입력
    u, v = map(int, input().split())  # u와 v는 연결된 두 노드
    graph[u].append(v)  # u에서 v로 가는 간선 추가
    graph[v].append(u)  # v에서 u로 가는 간선 추가 (양방향 그래프)

visited = [False] * (N + 1)  # 방문 여부를 저장하는 리스트 초기화 (1번 노드부터 사용)
count = 0  # 연결 요소의 개수를 저장하는 변수

for i in range(1, N + 1):  # 1번 노드부터 N번 노드까지 순회
    if not visited[i]:  # 현재 노드가 방문되지 않았다면
        dfs(i, visited, graph)  # DFS를 통해 연결된 모든 노드 방문
        count += 1  # 연결 요소 개수 증가

print(count)  # 연결 요소의 개수 출력
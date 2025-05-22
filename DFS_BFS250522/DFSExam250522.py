import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한을 늘려서 깊은 재귀 호출도 처리 가능하도록 설정
input = sys.stdin.readline  # 입력 속도 향상을 위한 설정
n, m = map(int, input().split())  # n: 노드 수, m: 간선 수

A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
    pass

for _ in range(m):
    s,e = map(int, input().split())
    A[s].append(e)  # s에서 e로 가는 간선 추가
    A[e].append(s)  # e에서 s로 가는 간선 추가 (양방향 그래프)

print("A=", A)

# 연결 요소의 개수 저장
count = 0
for i in range(1, n+1):  # 1번 노드부터 n번 노드까지 순회
    if not visited[i]:  # 현재 노드가 방문되지 않았다면
        DFS(i)  # DFS를 통해 연결된 모든 노드 방문
        count += 1  # 연결 요소 개수 증가
        DFS(i)  # DFS를 통해 연결된 모든 노드 방문

print("연결 요소의 개수:%d", count)  # 연결 요소의 개수 출력
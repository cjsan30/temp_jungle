# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

from collections import deque

computer = int(input())
line = int(input())
# con = [ tuple(map(int, input().split())) for _ in range(line)]

con = [[] for _ in range(computer+1)]

for _ in range(line):
    a, b = map(int, input().split())
    con[a].append(b)
    con[b].append(a)

# zombie : 감염 체크 현황(재탐색 방지)
# qu : 감염 처리된 목록
zombie = [False for _ in range(computer+1)]
qu = deque([1])
zombie[1] = True

while qu:
    zompc = qu.popleft() # 1
    
    for x in con[zompc]:
        if not zombie[x]:
            zombie[x] = True
            qu.append(x)

print(zombie.count(True)-1)
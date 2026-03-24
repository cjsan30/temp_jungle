# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

from collections import deque

areaN = int(input())
area = []
for _ in range(areaN):
    area.append(list(map(int, input().split())))
## BFS
visited = [[False] * areaN for _ in range(areaN)]
qu = deque()
qu.append((0,0))
visited[0][0] = True

while qu:
    y,x = qu.popleft()
    if y == areaN-1 and x == areaN-1:
        print("HaruHaru")
        break

    jump = area[y][x]
    if jump == 0: continue
    
    for jmy, jmx in [(jump,0), (0,jump)]:
        ry, rx = y+jmy, x+jmx
        if ry < areaN and rx < areaN and not visited[ry][rx]:
            visited[ry][rx] = True
            qu.append((ry,rx))
    
else:
    print("Hing")

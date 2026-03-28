# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725
from collections import deque
import sys
sys.setrecursionlimit(10**6)

nodenum =  int(input())

con = [[] for _ in range(nodenum+1)]

for _ in range(nodenum-1):
    a, b = map(int, input().split())
    con[a].append(b)
    con[b].append(a)
    
visited = [False] * (nodenum+1)
prnt = [[] for _ in range(nodenum+1)]
# prnt = [[0] * (nodenum+1)]

def dfs(now, visited):
    visited[now] = True
    for next in con[now]:
        if not visited[next]:
            prnt[next] = now
            dfs(next, visited)
    return prnt
            
dfs(1,visited)

for x in range(2, len(prnt)):
    print(prnt[x])
# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

limit = int(input())
innum = [x for x in range(limit)]

innum = list(map(int, input().split()))
rst = []

def chkprime():
    chk = True

    for i in range(limit):
        if innum[i] < 2: 
            continue
        if innum[i] == 2 or innum[i] == 3:
            rst.append(innum[i])
            continue

        chk = True

        for j in range(2, int(innum[i] ** 0.5)+1):
            if innum[i] % j == 0:
                chk = False
                break
        if chk:
            rst.append(innum[i])
                

chkprime()
print(len(rst))

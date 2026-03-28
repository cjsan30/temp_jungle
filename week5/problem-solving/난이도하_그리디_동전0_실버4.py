# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047


# cointype[::-1]
# total / cointype >> append total
# total % cointype[i]

(cointype, total) = tuple(map(int,input().split()))

result = 0
ct = []
for _ in range(cointype):
    ct.append(int(input()))
ct = ct[::-1]

for i in range(len(ct)):
    result = result + int(total / ct[i])
    total = total % ct[i]
   
print(result)
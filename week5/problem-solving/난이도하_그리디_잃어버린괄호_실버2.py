# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

# 양수 + - 구성된 식에서 () 추가해서 최소 값을 가진 식으로 변환

# input = 숫자(0~9), +, -

# '-' 기호 개수 : len - 1
expr = input().split('-')
rst =  (sum(map(int,expr[0].split('+'))))

for i in range(1,len(expr)):
    rst -= ((sum(map(int,expr[i].split('+')))))
    
print(rst)
    
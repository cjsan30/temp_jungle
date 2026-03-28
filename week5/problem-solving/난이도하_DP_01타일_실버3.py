# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

# 사소한 디테일 신경 안써서 수정 너무 많았음. 


# 0, 1 쓰여진 타일 선물 ( 아빠가 타일 공장장 )
# 1 , 00 타일   >> 01, 10 조합 불가 | 00 , 11

# 2진 수열의 개수 : t[n]    : 피보나치, Bottom-Up으로 접근
# 1     1   1
# 2     2   00,11
# 3     3   001,100,111
# 4     5   0000,0011,1001,1100,1111

# a = 1
# b = 2

# for _ in range(2, tile):
#     a, b = b, a+b
    
# print(b % 15746)

tile = int(input())
def dadtile(n):
    if n == 1: return 1

    t = [0] * (n+1)
    t[1] = 1
    t[2] = 2    

    for i in range(3, n+1):
        t[i] = (t[i-1] + t[i-2]) % 15746

    return t[n]

print(dadtile(tile))
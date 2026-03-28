# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

# 피보나치, 하향식 접근

cnt = int(input())

#### 하향식
# def recur_fibo(x, memo=None):
    
#     if memo == None: memo = {}
    
#     if x == 0: return 0
#     if x == 1: return 1
    
#     if x in memo: return memo[x]
    
#     memo[x] = recur_fibo(x-1, memo) + recur_fibo(x-2, memo)
    
#     return memo[x]

# print(recur_fibo(cnt))

#### 상향식
def bu_fibo(x):

    if x <= 1: return x

    dp = [0] * (x+1)
    dp[1] = 1
    
    for i in range(2, x+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[x]

print(bu_fibo(cnt))
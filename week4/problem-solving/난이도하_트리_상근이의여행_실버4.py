# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

# 가장 적은 종류 비행기 / 중복 가능 / 

# 3개의 국가 / 비행기 3 종류
# 1 2 2 3 1 3 
# 3국가 3종류면 1 <> 2 <> 3         --> 1 > 2 > 3 총 2개의 비행기
# 5개의 국가 / 비행기 4 종류
# 2 1 2 3 4 3 4 5
# 1 <> 2 <> 3 <> 4 <> 5             --> 1 > 2 > 3 > 4 > 5 총 4개의 비행기


# 전체 테스트 케이스
numcase = int(input())

# 국가의 수, 비행기의 종류
# country, flight = map(int, input().split())
for _ in range(numcase):
    country, flight = map(int, input().split())

# l = [tuple(map(int, input().split()))] 테스트
    line = [ tuple(map(int, input().split())) for _ in range(flight)]
    
    print(country-1)


    
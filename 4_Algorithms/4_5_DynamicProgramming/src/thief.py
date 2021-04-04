# https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    N = len(money)
    answer = 0
    
    dp = [0 for _ in range(N - 1)]
    dp[0], dp[1] = money[0], max(money[0], money[1])
    for i in range(2, N - 1):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])
    answer = dp[N - 2]
    
    dp = [0 for _ in range(N)]
    dp[0], dp[1] = 0, money[1]
    for i in range(2, N):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])
    answer = max(dp[N-1], answer)
    
    return answer
    
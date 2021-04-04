# https://www.acmicpc.net/problem/12865

N, K = map(int, input().split(' '))
W = [0] * N
V = [0] * N
for i in range(N):
    W[i], V[i] = map(int, input().split(' '))

dp = []
for _ in range(N):
    dp.append(dict())
    
def knapsack(i, w):
    if w in dp[i]:
        return dp[i][w]
    
    if i == -1 or w == 0:
        return 0
    
    if w >= W[i]:
        val = max(knapsack(i-1, w), knapsack(i-1, w-W[i]) + V[i])
    else:
        val = knapsack(i-1, w)
    
    dp[i][w] = val
    return val

print(knapsack(N-1, K))
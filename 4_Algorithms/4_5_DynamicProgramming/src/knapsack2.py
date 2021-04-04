# https://www.acmicpc.net/problem/12865

N, K = map(int, input().split(' '))
W = [0] * (N + 1)
V = [0] * (N + 1)
for i in range(1, N + 1):
    W[i], V[i] = map(int, input().split(' '))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, K + 1):
        if w >= W[i]:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-W[i]] + V[i])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[N][K])

N, K = map(int, input().split())

W = [0] * (N + 1)
V = [0] * (N + 1)

for i in range(1, N + 1):
    W[i], V[i] = map(int, input().split())

need_calc = [set() for _ in range(N + 1)]

need_calc[N].add(K)
for i in range(N, -1, -1):
    for w in need_calc[i]:
        if i == 0 or w == 0:
            continue

        if w >= W[i]:
            need_calc[i-1].add(w-W[i])
        need_calc[i-1].add(w)

dp = [[0 for _ in range(K + 1)] for _ in range(2)]
for i in range(1, N + 1):
    for w in need_calc[i]:
        if w >= W[i]:
            dp[i%2][w] = max(dp[(i-1)%2][w], dp[(i-1)%2][w-W[i]] + V[i])
        else:
            dp[i%2][w] = dp[(i-1)%2][w]

print(dp[N%2][K])

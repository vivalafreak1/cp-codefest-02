mod = 10**9 + 7
def bibit(N, K):
    if N == 1:
        return K
    dp = [K, K*K]
    for _ in range(2, N):
        dp.append((dp[-1] + dp[-2]) * (K-1) % mod)
    return dp[-1]
N, K = map(int, input().split())
print(bibit(N, K))

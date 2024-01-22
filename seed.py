mod = 10**9 + 7
def bit(N, K):
    if N == 1:
        return K
    ab = [[0] * K for _ in range(N)]
    for i in range(K):
        ab[0][i] = 1
    tot = K
    for i in range(1, N):
        tot_n = 0
        for j in range(K):
            ab[i][j] = (tot - ab[i-1][j] + mod) % mod
            tot_n = (tot_n + ab[i][j]) % mod
        tot = tot_n
    return tot
N, K = map(int, input().split())
hasil = bit(N, K)
print(hasil)

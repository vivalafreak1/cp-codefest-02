def esc(lab):
    N = len(lab)
    M = len(lab[0])
    if not (1 <= N <= 100 and 1 <= M <= 100):
        print("not valid")
        return False
    def exp(r, c):
        if r < 0 or c < 0 or r >= N or c >= M or lab[r][c] == '+' or v[r][c]:
            return False
        v[r][c] = True
        if r == N - 1 and c == M - 1:
            return True
        return exp(r + 1, c) or exp(r - 1, c) or exp(r, c + 1) or exp(r, c - 1)
    v = [[False] * M for _ in range(N)]
    return exp(0, 0)
N, M = map(int, input().split())
lab = []
for _ in range(N):
    lab.append(input())
if esc(lab):
    print("IYA")
else:
    print("TIDAK")

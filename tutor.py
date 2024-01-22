def maks(N, M, A):
    if not (1 <= N <= 10**2 and 1 <= M <= 10**3 and all(1 <= a <= 24 for a in A)):
        return "not valid"
    A.sort()
    hari = 0
    for i in range(N):
        if M >= A[i]:
            M -= A[i]
            hari += 1
        else:
            break
    return hari
N, M = map(int, input().split())
A = list(map(int, input().split()))
result = maks(N, M, A)
print(result)

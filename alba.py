def potongan(N):
    if N % 2 == 0:
        return N // 2
    else:
        return 1 + (N - 1) // 2

N = int(input())
hasil = potongan(N)
print(hasil)

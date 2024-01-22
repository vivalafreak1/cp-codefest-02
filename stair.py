def proses(n):
    jalan = [0] * (n + 1)
    jalan[0] = 1
    jalan[1] = 1
    for i in range(2, n + 1):
        jalan[i] = (jalan[i - 1] + jalan[i - 2]) % (10**9 + 7)
    return jalan[n]
n = int(input())
hasil = proses(n)
print(hasil)
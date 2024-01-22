def tangga(steps):
    return (steps * (steps + 1) // 2) - steps
n = int(input())
hasil = tangga(n)
print(hasil)

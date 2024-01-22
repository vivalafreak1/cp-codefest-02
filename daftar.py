def filter_nama(list_nama, target):
    array_nama = []
    for nama, grup in list_nama:
        if grup == target:
            array_nama.append(nama)
    return array_nama
N = int(input())
assert 1 <= N <= 10**3, "Batasan terlampaui: 1 <= N <= 10^3"
list_nama = []
for _ in range(N):
    nama, grup = input().split()
    assert 1 <= len(nama) <= 10**2, "Batasan terlampaui: 1 <= | A[i].size <= 10^2"
    assert len(grup) == 2 and grup[0].isdigit() and grup[1].isalpha(), "Batasan terlampaui: B[i] terdiri 2 karakter yang diawali dengan angka kemudian huruf"
    list_nama.append((nama, grup))
target = input()
array_nama = filter_nama(list_nama, target)
if array_nama:
    unique_nama = sorted(set(array_nama))
    for nama in unique_nama:
        print(nama)
else:
    print("Tidak Ada")
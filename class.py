def siswa(data, target):
    hasil_set = set()
    for nama, class_info in data:
        if class_info == target:
            hasil_set.add(nama)
    return sorted(list(hasil_set))
def main():
    N = int(input())
    data = []
    for _ in range(N):
        nama, class_info = input().split()
        data.append((nama, class_info))
    target = input().strip()
    kelas = siswa(data, target)
    if kelas:
        for student in kelas:
            print(student)
    else:
        print("Tidak Ada")
if __name__ == "__main__":
    main()

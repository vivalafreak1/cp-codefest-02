def potongan(N):
    total_potongan = N * (N + 1) // 2  
    if total_potongan % N == 0:
        return 0
    else:
        min_deductions = total_potongan % N  
        return min_deductions
N = int(input("Enter the number of pizza slices for Input #1: "))
hasil = potongan(N)
print(f"Expected Output #1: {hasil}")

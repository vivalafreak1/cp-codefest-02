def status(waktu):
    jam, menit = map(int, waktu.split(':'))
    if 18 <= jam < 24 or (jam == 18 and menit == 0) or 0 <= jam < 6:
        return "Matahari Tenggelam"
    else:
        return "Matahari Bersinar Terang"

str_input = input("")
hasil= status(str_input)
print(hasil)

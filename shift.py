def str(s, k):
    hasil = ""
    for char in s:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            enc_char = chr((ord(char) - base + k) % 26 + base)
            hasil += enc_char
        else:
            hasil += char
    return hasil
s = input().strip()
k = int(input().strip())
if 1 <= len(s) <= 100 and 1 <= k <= 25 and all(char.isalpha() and char.islower() for char in s):
    enc_str = str(s, k)
    print(enc_str)
else:
    print("Batasan terlampaui: error")

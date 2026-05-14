from ciphers.transposition import *

text1 = "żółta źółć"
encrypted = encrypt(text1, 3)
print(f"Tekst zaszyfrowany: {encrypted}")
print(f"Tekst odszyfrowawny: {decrypt(encrypted, 3)}")
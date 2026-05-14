import sys
import os

# Umożliwia import modułów z folderu głównego projektu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ciphers.transposition import encrypt, decrypt

text1 = "żółta źółć xyź 123* *#$@"
encrypted = encrypt(text1, 3)
print(f"Tekst zaszyfrowany: {encrypted}")
print(f"Tekst odszyfrowawny: {decrypt(encrypted, 3)}")
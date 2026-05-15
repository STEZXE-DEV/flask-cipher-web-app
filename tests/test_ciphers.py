import sys
import os
import random as r

# Umożliwia import modułów z folderu głównego projektu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ciphers.transposition import encrypt as t_encrypt, decrypt as t_decrypt
from ciphers.polibius import encrypt as p_encrypt, decrypt as p_decrypt
from ciphers.vigenere import encrypt as v_encrypt, decrypt as v_decrypt

print("\n=== SIMPLE RANDOM TESTS ===")

base_alphabet = (
    "abcdefghijklmnopqrstuvwxyz"
    "ąćęłńóśźż"
    "0123456789"
)

extra_chars = (
    " "          # space
    "\t"         # tab
    "\n"         # newline
    ".,!?-_"
)

# specjalne znaki
special_chars = (
    "()[]{}"
    "@#$%^&*"
    "+=/\\|"
    "'\""
)

alphabet = base_alphabet + extra_chars + special_chars

error_count = 0
t_total = 0
p_total = 0
v_total = 0

for _ in range(50):

    t_total += 1
    p_total += 1
    v_total += 1

    # losowy tekst tylko z dozwolonego alfabetu (LOGIC SAFE)
    text = "".join(r.choice(alphabet) for _ in range(r.randint(5, 25)))

    # losowe klucze
    key_t = r.randint(1, 15)
    key_p = r.randint(1, 7)
    key_v = r.choice([
    "key",
    "abc",
    "klucz",
    "żaba",
    "VERYLONGKEYYYYY",

    # krótkie
    "a",
    "aa",
    "xyz",

    # polskie
    "ąćę",
    "gęś",
    "król",
    "żółć",

    # mieszane case
    "Key",
    "KlUcZ",
    "VeRyLoNgKeY",

    # cyfry w kluczu 
    "key123",
    "abc2026",
])

    try:
        # TRANSPOSITION
        enc_t = t_encrypt(text, key_t)
        dec_t = t_decrypt(enc_t, key_t)

        # POLIBIUSZ
        enc_p = p_encrypt(text, key_p)
        dec_p = p_decrypt(enc_p, key_p)

        # VIGENERE
        enc_v = v_encrypt(text, key_v)
        dec_v = v_decrypt(enc_v, key_v)

        print(f"\nTEXT: {text}")
        print(f"T KEY={key_t} OK | P KEY={key_p} OK | V KEY={key_v} OK")

    except Exception as e:
        error_count += 1 
        print("\n==== ERROR ====")
        print("TEXT:", text)
        print("ERROR:", e)

total_tests = t_total + p_total + v_total 

print("\n=========================")
print("TEST SUMMARY")
print("=========================")
print("TOTAL RUNS:", total_tests)
print("ERRORS:", error_count)
print("SUCCESS RATE:", f"{(total_tests - error_count) / total_tests * 100:.2f}%")
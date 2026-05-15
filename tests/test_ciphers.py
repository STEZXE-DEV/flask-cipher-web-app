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

# licznik błędów
error_count = 0 # ogólny
t_err = 0 # dla transpozycji
p_err = 0 # dla polibiusza
v_err = 0 # dla vigenere

# licznik testów
t_total = 0 # transpozycji
p_total = 0 # polibiusza
v_total = 0 # vigenere



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

    except Exception as e:
        t_err += 1
        print("\n==== TRANSPOSITION ERROR ====")
        print("TEXT:", text)
        print(e)

    try:
        # POLIBIUSZ
        enc_p = p_encrypt(text, key_p)
        dec_p = p_decrypt(enc_p, key_p)

    except Exception as e:
        p_err += 1
        print("\n==== POLIBIUSZ ERROR ====")
        print("TEXT:", text)
        print(e)

    try:
        # VIGENERE
        enc_v = v_encrypt(text, key_v)
        dec_v = v_decrypt(enc_v, key_v)

    except Exception as e:
        v_err += 1
        print("\n==== VIGENERE ERROR ====")
        print("TEXT:", text)
        print(e)

total_tests = t_total + p_total + v_total 

print("\n=========================")
print("       TEST SUMMARY")
print("=========================\n")

print("TRANSPOSITION:")
print("  tests:", t_total)
print("  errors:", t_err)

print("POLIBIUSZ:")
print("  tests:", p_total)
print("  errors:", p_err)

print("VIGENERE:")
print("  tests:", v_total)
print("  errors:", v_err)

total_tests = t_total + p_total + v_total
total_errors = t_err + p_err + v_err

print("\nOVERALL:")
print("TOTAL:", total_tests)
print("ERRORS:", total_errors)
print("SUCCESS RATE:", f"{(total_tests - total_errors) / total_tests * 100:.2f}%")
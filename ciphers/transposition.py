import math as m
from .utility.util import normalize

# =========================
# SZYFR PRZESTAWIENIOWY
# =========================
# Kod odpowiada za szyfrowanie i deszyfrowanie metodą kolumnową (transposition)
# Klucz określa liczbę kolumn w macierzy


# =========================
# SZYFROWANIE
# =========================
def encrypt(message, key):

    # normalizacja tekstu:
    # - małe litery
    # - usunięcie spacji
    # - zamiana polskich znaków (np. ę -> e)
    message = normalize(message.lower().replace(" ", ""))

    message_length = len(message)

    # obliczenie liczby wierszy w macierzy
    matrix_rows = m.ceil(message_length / key)

    # tworzenie pustej macierzy
    message_matrix = [["" for _ in range(key)] for _ in range(matrix_rows)]

    message_letter_index = 0

    # wypełnianie macierzy wierszami
    for i in range(matrix_rows):
        for j in range(key):
            if message_letter_index < message_length:
                message_matrix[i][j] = message[message_letter_index]
                message_letter_index += 1

    encrypted_message = ""

    # odczyt kolumnami (kluczowy element szyfru)
    for j in range(key):
        for i in range(matrix_rows):
            encrypted_message += message_matrix[i][j]

    return encrypted_message


# =========================
# DESZYFROWANIE
# =========================
def decrypt(message, key):

    # normalizacja wejścia
    message = normalize(message.lower().replace(" ", ""))

    message_length = len(message)

    # obliczenie rozmiaru macierzy
    matrix_rows = m.ceil(message_length / key)

    # tworzenie pustej macierzy
    message_matrix = [["" for _ in range(key)] for _ in range(matrix_rows)]

    message_letter_index = 0
    decrypted_message = ""

    # wypełnianie macierzy kolumnami (odwrotność encrypt)
    for j in range(key):
        for i in range(matrix_rows):
            if message_letter_index < message_length:
                message_matrix[i][j] = message[message_letter_index]
                message_letter_index += 1

    # odczyt wierszami
    for i in range(matrix_rows):
        for j in range(key):
            decrypted_message += message_matrix[i][j]

    return decrypted_message

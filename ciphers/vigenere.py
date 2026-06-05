from .utility.util import normalize, cesar_encrypt, cesar_decrypt

# =========================
# SZYFR VIGENÈRE’A
# =========================
# Kod odpowiada za szyfrowanie i deszyfrowanie metodą Vigenère’a
# Wykorzystuje szyfr Cezara jako operację pomocniczą

# alfabet używany do wyznaczania przesunięć
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"


# =========================
# SZYFROWANIE
# =========================
def encrypt(message, key):

    # normalizacja tekstu:
    # - małe litery
    # - usunięcie spacji
    # - zamiana polskich znaków
    message = normalize(message.lower().replace(" ", ""))

    # normalizacja klucza
    key = normalize(key.lower().replace(" ", ""))

    # generowanie klucza powtarzanego (dopasowanie do długości wiadomości)
    key_string = ""

    for idx in range(len(message)):
        key_string += key[idx % len(key)]

    encrypted_message = ""

    # szyfrowanie znak po znaku
    for idx, letter in enumerate(message):

        # sprawdzenie czy znak klucza istnieje w alfabecie
        if key_string[idx] in alphabet:
            shift = alphabet.index(key_string[idx])
            encrypted_message += cesar_encrypt(letter, shift)

    return encrypted_message


# =========================
# DESZYFROWANIE
# =========================
def decrypt(message, key):

    # normalizacja tekstu wejściowego
    message = normalize(message.lower().replace(" ", ""))

    # normalizacja klucza
    key = normalize(key.lower().replace(" ", ""))

    # generowanie klucza powtarzanego
    key_string = ""

    for idx in range(len(message)):
        key_string += key[idx % len(key)]

    decrypted_message = ""

    # deszyfrowanie znak po znaku
    for idx, letter in enumerate(message):

        # sprawdzenie czy znak klucza istnieje w alfabecie
        if key_string[idx] in alphabet:
            shift = alphabet.index(key_string[idx])
            decrypted_message += cesar_decrypt(letter, shift)

    return decrypted_message

# =========================
# FUNKCJE POMOCNICZE
# =========================


# Funkcja do zamiany polskich znaków na podstawowe litery
def normalize(text):

    polish_dict = {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ź": "z",
        "ż": "z",
    }

    normalized_text = ""

    # zamiana znak po znaku
    for i in text:
        if i in polish_dict:
            normalized_text += polish_dict[i]
        else:
            normalized_text += i

    return normalized_text


# ===========================
# SZYFR CEZARA - SZYFROWANIE
# ===========================
def cesar_encrypt(message, key):

    # normalizacja i przygotowanie tekstu
    message = normalize(message.lower().replace(" ", ""))

    key %= 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    encrypted_message = ""

    # przesunięcie liter o wartość klucza
    for letter in message:
        if letter in alphabet:
            letter_position = (alphabet.index(letter) + key) % 26
            encrypted_message += alphabet[letter_position]

    return encrypted_message


# ==============================
# SZYFR CEZARA - DESZYFROWANIE
# ==============================
def cesar_decrypt(message, key):

    # normalizacja i przygotowanie tekstu
    message = normalize(message.lower().replace(" ", ""))

    key %= 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    decrypted_message = ""

    # cofanie przesunięcia
    for letter in message:
        letter_position = (alphabet.index(letter) - key) % 26
        decrypted_message += alphabet[letter_position]

    return decrypted_message

from .utility.util import normalize

# =========================
# SZYFR POLIBIUSZA
# =========================
# Kod odpowiada za szyfrowanie i deszyfrowanie tekstu
# przy użyciu siatki 6x6 (Polibiusz)

# Alfabet używany do budowy siatki 6x6
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"


def encrypt(message, key):
    # ograniczenie klucza do zakresu alfabetu
    key %= 36

    # przesunięcie alfabetu (działa jak prosty Caesar shift)
    shifted_alphabet = alphabet[key:] + alphabet[:key]

    # normalizacja tekstu:
    # - małe litery
    # - usunięcie spacji
    # - zamiana polskich znaków na podstawowe (np. ą -> a)
    message = normalize(message.lower().replace(" ", ""))

    # mapa znak -> pozycja w alfabecie
    position_dict = {}

    for i, letter in enumerate(shifted_alphabet):
        position_dict[letter] = i

    encrypted_message = ""

    # zamiana liter na współrzędne (wiersz + kolumna)
    for letter in message:
        if letter in alphabet:
            letter_position = position_dict[letter]
            column = letter_position % 6 + 1
            row = letter_position // 6 + 1

            encrypted_message += str(row) + str(column) + " "

    return encrypted_message


def decrypt(message, key):
    # ograniczenie klucza do zakresu alfabetu
    key %= 36

    # ten sam przesunięty alfabet co w encrypt
    shifted_alphabet = alphabet[key:] + alphabet[:key]

    # usunięcie spacji z zaszyfrowanej wiadomości
    message = message.replace(" ", "")

    decrypted_message = ""

    # odczyt par cyfr (wiersz, kolumna)
    for digit in range(0, len(message), 2):

        # UWAGA: zakładamy poprawne dane (walidacja powinna być wcześniej)
        number = [message[digit], message[digit + 1]]

        row = int(number[0]) - 1
        column = int(number[1]) - 1

        # przeliczenie współrzędnych na indeks w alfabecie
        letter_position = row * 6 + column

        decrypted_message += shifted_alphabet[letter_position]

    return decrypted_message

from .utility.util import normalize, cesar_encrypt, cesar_decrypt

# Kod odpowiadający za logikę szyfrowania i deszyfrowania metodą Vigener'a

alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(message, key):
    message =  normalize(message.lower().replace(" ", ""))

    key = normalize(key.lower().replace(" ", ""))
    key_string = ''

    for idx in range(len(message)):
        key_string += key[idx % len(key)]

    encrypted_message = ''

    for idx, letter in enumerate(message):
        if key_string[idx] in alphabet:
            encrypted_message += cesar_encrypt(letter, alphabet.index(key_string[idx]))

    return encrypted_message

def decrypt(message, key):
    message =  normalize(message.lower().replace(" ", ""))
    key = normalize(key.lower().replace(" ", ""))
    key_string = ''

    for idx in range(len(message)):
        key_string += key[idx % len(key)]

    decrypted_message = ''

    for idx, letter in enumerate(message):
        if key_string[idx] in alphabet:
            decrypted_message += cesar_decrypt(letter, alphabet.index(key_string[idx]))

    return decrypted_message
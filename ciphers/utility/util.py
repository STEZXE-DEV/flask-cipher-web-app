
# Funkcja służąca do normalizacji (podmiany) polskich znaków diakrytycznych
def normalize(text):
    polish_dict = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ź': 'z',
    'ż': 'z'
}
    normalized_text = ''
    for i in text:
        if i in polish_dict:
            normalized_text += polish_dict[i]
        else:
            normalized_text += i

    return normalized_text

def cesar_encrypt(message, key):

    message =  normalize(message.lower().replace(" ", ""))

    key %= 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    encrypted_message = ''

    for letter in message:
        letter_position = (alphabet.index(letter) + key) % 26
        encrypted_message += alphabet[letter_position]
    
    return encrypted_message

def cesar_decrypt(message, key):

    message =  normalize(message.lower().replace(" ", ""))

    key %= 26
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    encrypted_message = ''

    for letter in message:
        letter_position = (alphabet.index(letter) - key) % 26
        encrypted_message += alphabet[letter_position]
    
    return encrypted_message
from .utility.util import normalize

# Kod odpowiadający za logikę szyfrowania i deszyfrowania metodą Polibiusza

# Alfabet bazowy, który pozwala na stworzenie siatki 6x6
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

def encrypt(message, key):

    key %= 36
    shifted_alphabet = alphabet[key:] + alphabet[:key]

    # zamiana liter wiadomości na małe litery, usunięcie spacji i normalizacja polskich znaków diakrytycznych
    message =  normalize(message.lower().replace(" ", ""))

    position_dict = {}
    
    for i, letter in enumerate(shifted_alphabet):
        position_dict[letter] = i

    encrypted_message = ''

    for letter in message:
        if letter in alphabet:
            letter_position = position_dict[letter]
            column = letter_position % 6 + 1
            row = letter_position // 6 + 1
            encrypted_message += str(row) + str(column) + ' '
    
    return encrypted_message

def decrypt(message, key):

    key %= 36
    shifted_alphabet = alphabet[key:] + alphabet[:key]

    message = message.replace(" ", "")

    decrypted_message = ''

    for digit in range(0, len(message), 2):

        '''WAŻNE: wymaga walidacji w backendzie, bo jeśli będzie nieparzysta długość wiadomości to wystąpi IndexError w message[digit+1]'''
        number = [ message[digit], message[digit+1] ]   
        row = int(number[0]) - 1
        column = int(number[1]) - 1
        letter_position = row * 6 + column
        decrypted_message += shifted_alphabet[letter_position]

    return decrypted_message
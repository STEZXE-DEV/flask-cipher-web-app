import math as m

# Kod odpowiadający za logikę szyfrowania i deszyfrowania metodą przestawieniową - skokową


# Funkcja szyfrowania
# klucz jest ilością kolumn, wedle której następuje podział wiadomości
def encrypt(message, key):

    message = message.lower().replace(" ", "")
    message_length = len(message)
    matrix_rows = m.ceil(message_length / key)
    message_matrix = [['' for _ in range(key)] for _ in range(matrix_rows)]
    message_letter_index = 0

    for i in range(matrix_rows):
        for j in range(key):
            if message_letter_index < message_length:
                message_matrix[i][j] = message[message_letter_index]
                message_letter_index += 1


    encrypted_message = ''

    for j in range(key):
        for i in range(matrix_rows):
            encrypted_message += message_matrix[i][j]

    return encrypted_message

# Funkcja deszyfrowania     
def decrypt(message, key):
    
   
    message = message.lower().replace(" ", "")
    message_length = len(message)
    matrix_rows = m.ceil(message_length / key)
    message_matrix = [['' for _ in range(key)] for _ in range(matrix_rows)]
    message_letter_index = 0
    decrypted_message = ''

    for j in range(key):
        for i in range(matrix_rows):
            if message_letter_index < message_length:
                message_matrix[i][j] = message[message_letter_index]
                message_letter_index += 1

    for i in range(matrix_rows):
        for j in range(key):
            decrypted_message += message_matrix[i][j]
                
    return decrypted_message
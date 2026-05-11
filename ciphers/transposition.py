import textwrap as tx

# Kod odpowiadający za logikę szyfrowania i deszyfrowania metodą przestawieniową - skokową

def encrypt(message, key):

    message = message.lower()
    message = message.replace(" ", "")
    message_length = len(message)
    message_columns = ['' for x in range(key)]   

    for i in range(message_length):
        message_columns[i % key] += message[i]
    encrypted_message = ''.join(message_columns)

    return encrypted_message

    
def decrypt(message, key):
    
    decrypted_message = ''
    message = message.lower()
    message = message.replace(" ", "")
    message_length = len(message)
    message_columns = [ x for x in tx.wrap(message, key)]
    print(message_columns)

    for i in range(len(message_columns[0])):
        for column in message_columns:
            decrypted_message += column[i]

    decrypted_message = ''.join(decrypted_message)
    return decrypted_message


# text1 = "żółta źółć"
# print(encrypt(text1, 3))
print(decrypt("żtóóałłźć", 3))
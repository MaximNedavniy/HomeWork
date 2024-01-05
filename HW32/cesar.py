def caesar_encryption(shift, message):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in message.upper():
        location = alphabet.find(i)
        new_location = location + shift
        if i in alphabet:
            result += alphabet[new_location]
        else:
            result += i
    print(result)
    return result

def caesar_decryption(shift, message):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in message.upper():
        location = alphabet.find(i)
        new_location = location - shift
        if i in alphabet:
            result += alphabet[new_location]
        else:
            result += i
    print(result)


# caesar_encryption(3, "Hello")
# caesar_decryption(3, "KHOOR")

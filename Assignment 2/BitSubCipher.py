def encrypt(plaintext, shift):
    if shift > len(plaintext):
        raise ValueError("Shift is longer than the message it is shifting")
    binary_text = ""
    ciphertext = ""
    for char in plaintext:
        binary_text += ''.join(format(ord(char), 'b')).replace(" ", "")
    shift_bits = binary_text[:shift]
    binary_text = binary_text[shift+1:]
    binary_text = binary_text + shift_bits
    ciphertext += ''.join(chr(int(binary_text[i * 8:i * 8 + 8], 2)) for i in range(len(binary_text) // 8))

    return ciphertext


def decrypt(ciphertext, shift):
    if shift > len(ciphertext):
        raise ValueError("Shift is longer than the message it is shifting")
    plaintext = ""
    binary_text = ""
    for char in ciphertext:
        binary_text += ''.join(format(ord(char), 'b'))
    shift_bits = binary_text[-shift:]
    binary_text = binary_text[:-shift]
    binary_text = shift_bits + binary_text
    plaintext += ''.join(chr(int(binary_text[i * 8:i * 8 + 8], 2)) for i in range(len(binary_text) // 8))
    return plaintext


message = "This is Sparta!!"
shift = 7

plain_binary, encrypted_message = encrypt(message, shift)
print(encrypted_message)

decrypt_binary, decrypted_message = decrypt(encrypted_message, shift)
print(decrypted_message)



def caesar_cipher_ascii(text, shift):
    result = ""
    for ch in text:
        ascii_val = ord(ch)
        if 32 <= ascii_val <= 126:
            new_val = 32 + ((ascii_val - 32 + shift) % 95)
            result += chr(new_val)
        else:
            result += ch
    return result


def caesar_decipher_ascii(text, shift):
    return caesar_cipher_ascii(text, -shift)


# Contoh penggunaan
plaintext = "2m{y!\"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0"
shift = -1 

while(True) :
    ciphertext = caesar_cipher_ascii(plaintext, shift)
    #decrypted = caesar_decipher_ascii(ciphertext, shift)

    #print("Plaintext :", plaintext)
    print(shift, end="")
    print("Ciphertext:", ciphertext)
    #print("Decrypted :", decrypted)
    shift-=1
    if shift == -100:
        break

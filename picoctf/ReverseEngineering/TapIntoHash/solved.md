# TITLE : Tap Into Hash
## Author : NGIRIMANA Schadrack
## Description
In this challenge, we were given a Python file that encrypts a user-supplied string using a custom blockchain construction combined with XOR-based encryption.

The relevant encryption function is shown below:
```py
def encrypt(plaintext, inner_txt, key):
    midpoint = len(plaintext) // 2

    first_part = plaintext[:midpoint]
    second_part = plaintext[midpoint:]
    modified_plaintext = first_part + inner_txt + second_part
    block_size = 16
    plaintext = pad(modified_plaintext, block_size)
    key_hash = hashlib.sha256(key).digest()
    print(key_hash)
    ciphertext = b''

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        cipher_block = xor_bytes(block, key_hash)
        ciphertext += cipher_block

    return ciphertext
```
The program inserts our input string into the middle of the blockchain hash string, applies PKCS-style padding, hashes the provided key using SHA-256, and then encrypts the entire plaintext using a repeating XOR with the hashed key.

Importantly, the same SHA-256 key stream is reused for every 16-byte block, which makes this construction cryptographically insecure.     
The challenge also provided:
- The final ciphertext
- The encryption key
Because XOR encryption is symmetric, decryption can be performed by applying the same XOR operation again with the same key.    
I reversed the encryption logic and implemented the following decryption function:
```py
def decrypt(ciphertext, key):
    block_size = 16
    key_hash = hashlib.sha256(key).digest()

    plaintext = b''

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i+block_size]
        plain_block = xor_bytes(block, key_hash)
        plaintext += plain_block

    return plaintext
```
After running the script with the provided ciphertext and key, I successfully recovered the original plaintext, which contained the flag.

def mod_inverse(a, m):
    # Since 41 is prime, we can use Fermat's Little Theorem:
    # The modular inverse is a^(m-2) mod m.
    return pow(a, m - 2, m)

def decrypt_message(nums):
    modulus = 41
    message = ""
    for num in nums:
        # Take each number mod 41.
        remainder = num % modulus
        # Find the modular inverse of the remainder mod 41.
        inv = mod_inverse(remainder, modulus)
        # Map the modular inverse to a character:
        if 1 <= inv <= 26:
            # 1->A, 2->B, ... 26->Z (ASCII: A is 65)
            message += chr(inv + 64)
        elif 27 <= inv <= 36:
            # Map 27->0, 28->1, ..., 36->9
            message += str(inv - 27)
        elif inv == 37:
            message += "_"
    return message

nums = [432, 331, 192, 108, 180, 50, 231, 188, 105, 51, 364, 168, 344, 195, 297, 342, 292, 198, 448, 62, 236, 342, 63]
print(decrypt_message(nums))

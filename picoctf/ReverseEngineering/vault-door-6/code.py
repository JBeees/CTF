encrypted = [110,48,116,95,109,85,99,72,95,104,52,114,68,51,114,95,
             116,72,52,110,95,120,48,114,95,57,53,98,101,53,100,99]

decrypted = ''.join(chr(b) for b in encrypted)
print(decrypted)


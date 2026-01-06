# TITLE : The Keymaker
## Author : kcbowhunter
## Description
Jpeg comments can be very interesting.
## Solution
In this challenge, we are given a JPEG file.

I started by running strings on the image and found the following Base64-encoded data:
```
b3BlbnNzbCBlbmMgLWQgLWFlcy0yNTYtY2JjIC1pdiBTT0YwIC1LIFNPUyAtaW4gZmxhZy5lbmMg
LW91dCBmbGFnIC1iYXNlNjQKCml2IGRvZXMgbm90IGluY2x1ZGUgdGhlIG1hcmtlciBvciBsZW5n
dGggb2YgU09GMAoKa2V5IGRvZXMgbm90IGluY2x1ZGUgdGhlIFMwUyBtYXJrZXIKCg==
```
Decoding it gives:
```
openssl enc -d -aes-256-cbc -iv SOF0 -K SOS -in flag.enc -out flag -base64
iv does not include the marker or length of SOF0
key does not include the S0S marker
```
This tells us that the challenge uses AES-256-CBC decryption and provides hints on how to derive the IV and key from the JPEG structure.    
#### Interpreting the Hint
- SOF0 (Start of Frame 0) and SOS (Start of Scan) are JPEG markers, not literal values.
- They indicate where to extract bytes from the JPEG file.

#### IV derivation

- AES-CBC requires a 16-byte IV
- The IV is taken from the `SOF0` segment payload
- The following bytes are excluded:
    - `SOF0` marker (FF C0)
    - `SOF0` length field (2 bytes)

- We take the next 16 bytes after those fields

#### Key derivation
- AES-256 requires a 32-byte key
- The key is taken from data after the SOS marker
- The SOS marker `FF DA` itself is excluded
- We take the next 32 bytes

#### Encrypted Data
Another string found in the image is:
```
CmmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY
```
This string is Base64-encoded ciphertext.
The leading `C` is intentionally misleading and should be ignored.

Save the corrected Base64 data into a file called `flag.enc`.
#### Final Decryption Command
After extracting the correct IV and key from the JPEG and converting them to hexadecimal, the final command becomes:
```
openssl enc -d -aes-256-cbc -iv 0800be00c803011100021101031101ff -K 000c03010002110311003f00f9766bfc44beda8f3f5c031b92cb0e92d6bdc952 -in flag.enc -out flag -base64
```
Running this command successfully decrypts the file and reveals the flag.

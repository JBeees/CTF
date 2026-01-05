# TITLE : HailCaesar!
## Author : kcbowhunter 
## Description
You might need to write some Python to solve this challenge. Some encryption may be involved. Good Luck!
## Solution
In this challenge, we are given a JPG file.
The first step is to inspect the file using the strings utility to identify any readable embedded data.

From the output, the following strings are extracted:
```
CTFlearn{Hail_Caesar!!!}
CTFlearn{Airplanes_Sometimes_Cause_Inflight_Incidents}
CTFlearn{Flight_32_Leaves_soon_from_gate_126}
B/<V5;)j}j6\<Y)8><\9Fbu,Hy4ONC}pxP"4st12wn`?@O$6BgQo7i#gtD|s>3lf=
iSWYgeW91IGFyZSBoYXZpbmcgdHJvdWJsZSBzb2x2aW5nIHRoaXMgY2hhbGxlbmdlLCBwbGVhc2Ug
c29sdmUgbXkgb3RoZXIKY2hhbGxlbmdlcyBmaXJzdDoKUnViYmVyRHVjawpTbm93Ym9hcmQKUGlr
ZXNQZWFrCkdhbmRhbGZUaGVXaXNlCgpUaGUgY2hhbGxlbmdlcyBhcmUgZGVzaWduZWQgdG8gYmUg
aW5jcmVhc2luZyBpbiBkaWZmaWN1bHR5IGFuZCB0aGlzIEhhaWxDYWVzYXIgY2hhbGxlbmdlIGlz
IHRoZSBuZXh0CmNoYWxsZW5nZSBpbiB0aGUgc2VyaWVzLgoKTXkgVHdpdHRlciBETSBpcyBvcGVu
IEBrY2Jvd2h1bnRlciBidXQgcGxlYXNlIG9ubHkgcGluZyBtZSBpZiB5b3UgaGF2ZSBzb2x2ZWQg
dGhlIGFib3ZlIGNoYWxsZW5nZXMgZmlyc3QuCgpJZiB5b3UgYXJlIG5ldyB0byB0aGUganBlZyBm
aWxlIGZvcm1hdCBwbGVhc2UgcmVhZCB0aGlzOgpodHRwczovL2Rldi5leGl2Mi5vcmcvcHJvamVj
dHMvZXhpdjIvd2lraS9UaGVfTWV0YWRhdGFfaW5fSlBFR19maWxlcwoKSWYgeW91IGFyZSBuZXcg
dG8gaGFja2luZyBhbmQgYXJlIHN0aWxsIGxlYXJuaW5nIGFib3V0IGJpdHMgYW5kIGJ5dGVzIHBs
ZWFzZSB3YXRjaCB0aGlzIHZpZGVvOgpodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PXRM
ZHZFT2FtM3NrCgp4b3JwZCBoYXMgYSBsb3Qgb2YgZnJlZSB2aWRlb3MgdGhhdCB0ZWFjaCBpbXBv
cnRhbnQgY29tcHV0ZXIgc2NpZW5jZSAvIGhhY2tpbmcgY29uY2VwdHMuCgpOb3RlIHRoYXQgb2Z0
ZW4gbXkgY2hhbGxlbmdlcyBjb21iaW5lIGZvcmVuc2ljcyBhbmQgc29tZSBhc3BlY3Qgb2YgY3J5
cHRvZ3JhcGh5LgoKSGF2ZSBmdW4hCmtjYm93aHVudGVyCgoK
42m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0
```
Observations

1. Several strings are wrong flags, indicating a Caesar Cipher–themed challenge.    
2. One large block of text is Base64-encoded, which can be decoded to obtain hints.    
3. Two strings appear to be encrypted using a non-alphabetic Caesar cipher, notably:   
```
B/<V5;)j}j6\<Y)8><\9Fbu,Hy4ONC}pxP"4st12wn`?@O$6BgQo7i#gtD|s>3lf=
2m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0
```
One of the decoded flags explicitly mentions:
```
Flight_32_Leaves_soon_from_gate_126
```
This strongly suggests that the cipher operates over the printable ASCII range, from 32 to 126.
**Cipher Logic**

Printable ASCII characters range from:
- 32 (space) to 126 (~)
- Total characters: 95
Therefore, the cipher is a printable-ASCII Caesar cipher, not a standard alphabetic one.
```
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
```
By testing all possible shifts in the printable ASCII range, the correct flag is revealed at: `shift = -18` At this shift, the decrypted output becomes a valid and readable CTFlearn flag.

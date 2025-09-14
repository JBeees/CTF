# TITLE : vault-door-6
## Author : Mark E. Haase
## Description
This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](https://jupiter.challenges.picoctf.org/static/cdb33ffba609e2521797aac66320ec65/VaultDoor6.java)
## Hints 
- If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.
## Solution
We were given a Java file where the password is validated using the following XOR process:
```java
for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
}
```
This is equivalent to computing the correct input for each byte as:
```java
passBytes[i] = myBytes[i] ^ 0x55; 
```
So to recover the flag:

1. We take the stored myBytes values from the program.  
2. We reverse the XOR by computing myBytes[i] ^ 0x55 for each byte.   
3. The resulting byte array is the password (or the flag).  

**Python script to decode**
```python
encrypted = [110,48,116,95,109,85,99,72,95,104,52,114,68,51,114,95,
             116,72,52,110,95,120,48,114,95,57,53,98,101,53,100,99]

decrypted = ''.join(chr(b) for b in encrypted)
print(decrypted)
```


# TITLE : My Friend John
## Author : Namespace
## Description
Have you met my friend John?

He's not so scary, even though they call him "The Ripper".
## Solution
In this challenge, we were given a ZIP file. When attempting to extract it, the archive prompted for a password. Each stage required cracking the ZIP password using John the Ripper, and the challenge consisted of three sequential steps.

In the first step, the ZIP password was cracked using the RockYou wordlist:
```
zip2john use-rockyou.zip > thehash.hash
john thehash.hash --wordlist=/usr/share/wordlists/rockyou.txt
```
After extracting the first archive, a second password-protected ZIP file was obtained. This time, the password was cracked using a custom wordlist:
```
zip2john custom-list.zip > custom.hash
john custom.hash --wordlist=custom-list.txt
```
In the final step, the ZIP file was protected with a numeric PIN-based password, requiring a brute-force approach. I generated a wordlist containing all possible 4-digit and 6-digit PINs using the following Python script:
```py
def generate_pins(filename: str):
    with open(filename, "w") as f:
        # 4-digit PINs: 0000–9999
        for i in range(10000):
            f.write(f"{i:04d}\n")

        # 6-digit PINs: 000000–999999
        for i in range(1000000):
            f.write(f"{i:06d}\n")


generate_pins("pins.txt")
```
This wordlist was then used to crack the final ZIP password:
```
zip2john brute-force-pin.zip > pin.hash
john pin.hash --wordlist=pins.txt
```
Successfully cracking the final archive revealed the flag file, which contained the challenge flag.

# TITLE : Brute Force is Fun!
## Author : yuvalm
## Description
You'll need Brute Force to solve this. Knowing Python should help too. Oh! And Base64 encryption of course! Find the flag!

https://mega.nz/#!vf43RCyC!NNpuYjB3d-gevhsHXefwAAAmzk4tJHxUZr0GnrSDI_c Hash: e82a4b4a0386d5232d52337f36d2ab73
## Solution
In this challenge, we are given a JPG file. When I ran binwalk on the file, I discovered that it contained embedded data. I extracted the embedded content using:
```
binwalk -e <jpg_name>
```
After extraction, I obtained:
- A password-protected ZIP file
- A folder containing many nested directories
To locate any interesting files inside those directories, I searched recursively using:
```
find . -type f
```
From the output, I found two suspicious files:
```
./_legotroopers.jpg.extracted/folders/73/47/p
./_legotroopers.jpg.extracted/folders/73/43/p
```
When I examined the contents of one of these files, it contained the following hint:
```
Hmmm... almost!
The password is: "ctflag*****" where * is a number.
Encrypt the password using MD5 and compare it to the given hash!
As I said, you're gonna have to brute force the password!
Good luck! :)
```
This indicates that the ZIP password follows the format `ctflagXXXXX`, where `XXXXX` is a 5-digit number, possibly including leading zeros. The correct password must be found by brute-forcing the MD5 hash.
#### Brute Force Script

I wrote the following Python script to brute-force the password:
```py
import hashlib
hash_check = "e82a4b4a0386d5232d52337f36d2ab73"
for i in range(100000):
    s = str(i).zfill(5)
    testing = "ctflag"+str(i)
    if hashlib.md5(testing.encode()).hexdigest() == hash_check:
        print("Found:", i)
        break
    print(s)
```
Once the correct password was found, I used it to unlock the ZIP file.
After extracting the contents of the unlocked ZIP file, I found another ZIP file containing a flag file. The flag file held a Base64-encoded string.

I decoded the Base64 string, which revealed the final flag.

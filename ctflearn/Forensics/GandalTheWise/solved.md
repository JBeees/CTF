# TITLE : GandalfTheWise
## Author : kcbowhunter
## Description
Extract the flag from the Gandalf.jpg file. You may need to write a quick script to solve this.
## Solution
In this challenge, we were given a JPG file. I first used the strings utility to extract readable data from the file and obtained the following three strings:
```
+Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo=
+xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p
+h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU
```
The first string is Base64-encoded. After decoding it, I obtained:
```
CTFlearn{xor_is_your_friend}
```
This value is not the real flag; instead, it serves as a hint indicating that an XOR operation is required.

To obtain the actual flag, I Base64-decoded the second string and then applied an XOR operation using the decoded result as the input and the third string (Base64-decoded) as the XOR key:
```
base64(decoded as an input) XOR third_string(as a key)
```
This XOR operation produced the real flag, completing the challenge.

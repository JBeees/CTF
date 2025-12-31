# TITLE : Minions
## Author : TedZak
## Description
Hey! Minions have stolen my flag, encoded it few times in one cipher, and then hidden it somewhere there: https://mega.nz/file/1UBViYgD#kjKISs9pUB4E-1d79166FeX3TiY5VQcHJ_GrcMbaLhg Can you help me? TIP: Decode the flag until you got a sentence.
## Solution
In this challenge, we were given a PNG file. When I inspected the file using `xxd`, I noticed indicators of an embedded file within the image. To extract the hidden content, I used binwalk:
```
binwalk -e <png_name>
```
Inside the extracted directory, there was a text file `..txt` containing a link to another image. After downloading that image, I again identified embedded data within it and repeated the extraction process using binwalk.

This process produced an image named `YouWon(Almost).jpg`. I then used strings on this image and discovered a Base64-encoded string:
```
VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0=
```
The string required multiple rounds of Base64 decoding. After decoding it repeatedly, the final plaintext revealed the flag, completing the challenge.

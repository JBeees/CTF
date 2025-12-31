# TITLE : Digital Camouflage
## Author : skywalkrs
## Description
We need to gain access to some routers. Let's try and see if we can find the password in the captured network data: https://mega.nz/#!XDBDRAQD!4jRcJvAhMkaVaZCOT3z3zkyHre2KHfmkbCN5lYpiEoY Hint 1: It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?<br /> Hint 2: If you think you found the flag, but it doesn't work, consider that the data may be encrypted.

Credit: picoCTF 2017
In this challenge, we were given a .pcap file. I first used the strings utility to extract readable text from the capture. From the output, I observed that a user was attempting to log in to a web page, based on the following request parameters:
```
userid=hardawayn&pswrd=UEFwZHNqUlRhZQ%3D%3Dv
```
The value of the `pswrd` parameter appeared to be URL-encoded. After URL-decoding it, the value became:
```
UEFwZHNqUlRhZQ==
```
This string is Base64-encoded. Decoding it revealed the plaintext value, which corresponds to the flag, completing the challenge.

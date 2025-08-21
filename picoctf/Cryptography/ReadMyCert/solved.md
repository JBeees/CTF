# TITLE : ReadMyCert
## Author : Sunday Jacob Nwanyim
## Description
How about we take you on an adventure on exploring certificate signing requests
Take a look at this CSR file [here](https://artifacts.picoctf.net/c/426/readmycert.csr).
## Hints
- Download the certificate signing request and try to read it.
## Solution
In this challenge, we are given a .csr file. Since a CSR file is encoded in Base64 (PEM format), we just need to decode the Base64 text. After decoding, we obtain the flag.

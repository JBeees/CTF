# TITLE : QR Code
## Author : severus
## Description
Do you remember something known as QR Code? Simple. Here for you : <br /> https://mega.nz/#!eGYlFa5Z!8mbiqg3kosk93qJCP-DBxIilHH2rf7iIVY-kpwyrx-0
## Solution
In this challenge, we were given a QR code image (PNG).
After scanning the QR code, it revealed a text string.

The text was encoded, so I decoded it using Base64 and then applied ROT13.
After decoding both layers, the original message was revealed, which contained the flag.

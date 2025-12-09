# TITLE : Flag in Flame
## Author : Prince Niyonshuti N.
## Description
The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log.
Download the encoded data here: [Logs Data](https://challenge-files.picoctf.net/c_amiable_citadel/929daf6ef01bba32b165e0a7c649ff4c953f2af21c28b024e8af5276b7716de5/logs.txt). Be prepared—the file is large, and examining it thoroughly is crucial.
## Hints
- Use base64 to decode the data and generate the image file.
## Solution
In this challenge, we were given an encoded log file. The hint mentioned that it was Base64-encoded, so I decoded it using:
```
base64 -d logs.txt > output
```
The decoded output turned out to be a PNG image. When I opened the PNG file, I saw a long sequence of numbers inside the image. I used **Google Lens** to extract the text, and I noticed that the sequence was in hexadecimal format.

I then used **CyberChef** to decode the extracted hex string. After converting it from hex to text, I obtained the flag.

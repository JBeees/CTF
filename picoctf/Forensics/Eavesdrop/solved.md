# TITLE : Eavesdrop
## Author : LT 'syreal' Jones
## Description
Download this packet capture and find the flag.
[Download packet capture](https://artifacts.picoctf.net/c/133/capture.flag.pcap)
## Hints
- All we know is that this packet capture includes a chat conversation and a file transfer.
## Solution
In this challenge, we were given a .pcap file. I opened it in Wireshark and inspected the TCP streams by right-clicking → Follow → TCP Stream. In the 0th TCP stream, I found a chat log:
```
Hey, how do you decrypt this file again?
You're serious?
Yeah, I'm serious
*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
Ok, great, thanks.
Let's use Discord next time, it's more secure.
C'mon, no one knows we use this program like this!
Whatever.
Hey.
Yeah?
Could you transfer the file to me again?
Oh great. Ok, over 9002?
Yeah, listening.
Sent it
Got it.
You're unbelievable
```
From this conversation, I learned two key things:
- The file was encrypted with OpenSSL DES3, using the password supersecretpassword123.
- The file was transferred over TCP port 9002.

Next, I applied the Wireshark display filter:
```
tcp.port == 9002
```
This revealed the file transfer. The data began with the expected Salted__ header, confirming it was an OpenSSL-encrypted file. I saved the stream as Raw and named it enc.des3.

Finally, I decrypted the file using the command mentioned in the chat:
```
openssl des3 -d -salt -in enc.des3 -out file.txt -k supersecretpassword123
```
This produced the decrypted output in file.txt. Inside, I found the flag.

# TITLE : A CAPture of a Flag
## Author : hazzy
## Description
This isn't what I had in mind, when I asked someone to capture a flag... can you help? You should check out WireShark.
## Solution
In this challenge, we were given a .pcap file containing network packets. I first analyzed the capture using Wireshark, but no obvious flag or suspicious activity was visible through standard inspection.

Next, I used a command-line approach to extract potential HTTP GET requests directly from the capture file:
```
strings flag.pcap | grep -i "GET /"
```
This command searches for printable strings within the pcap and filters lines that resemble HTTP GET requests.

From the output, I found the following request:
```
GET /?msg=ZmxhZ3tBRmxhZ0luUENBUH0= HTTP/1.1
```
The value of the msg parameter appeared to be Base64-encoded. After decoding it, the plaintext revealed the flag, completing the challenge.


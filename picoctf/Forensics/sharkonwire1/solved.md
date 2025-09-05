# TITLE : shark on wire 1
## Author : Danny
## Description
We found this packet capture. Recover the flag.
## Hints
- Try using a tool like Wireshark
- What are streams?
## Solution
In this challenge, we were given a .pcap file, so I opened it in Wireshark. The hint mentioned looking at the streams, so I right-clicked on a packet and selected Follow → UDP Stream. By checking stream number 6, I was able to find the flag.


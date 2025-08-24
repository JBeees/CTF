# TITLE : Ph4nt0m 1ntrud3r
## Author : Prince Niyonshuti N.
## Description
A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag.
To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder!
Find the PCAP file here [Network Traffic PCAP file](https://challenge-files.picoctf.net/c_verbal_sleep/a681faccaaa199ce75c3abeef9525f813b6451644a8d8d27cc097e4b1ccb741a/myNetworkTraffic.pcap) and try to get the flag.
## Hints
- Filter your packets to narrow down your search.
- Attacks were done in timely manner.
- Time is essential
## Solution
In this challenge, we are given a .pcap file. I used Wireshark to analyze it and look for the flag. The capture contained 22 packets.
By inspecting each packet in detail, I noticed that the TCP segment data contained base64-encoded strings, such as: 
```
ezF0X3c0cw==
```
When decoded from base64, this produced:
```
{1t_w4s
```
I continued checking the other packets and found additional fragments of the flag. Each piece of the flag appeared in packets where the payload length was either 12 or 4 bytes. After collecting and combining all of these base64 fragments, I successfully reconstructed the full flag.

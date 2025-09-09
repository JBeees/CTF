# TITLE : FindAndOpen
## Author : Mubarak Mikail
## Description
Someone might have hidden the password in the trace file.
Find the key to unlock [this file](https://artifacts.picoctf.net/c/495/flag.zip). [This tracefile](https://artifacts.picoctf.net/c/495/dump.pcap) might be good to analyze.
## Hints
- Download the pcap and look for the password or flag.
- Don't try to use a password cracking tool, there are easier ways here.
## Solution
In this challenge, we were given a .zip file and a .pcap file. The .zip file required a password to extract its contents. The password could be found within the .pcap file.

I analyzed the .pcap file using the `strings` command and discovered an encrypted Base64 string. After decoding it, I obtained part of the flag. I then used this decoded value as the password for the .zip file.

Upon extracting the .zip file, I found the complete flag inside.

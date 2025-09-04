# TITLE : WPA-ing Out
## Author : MistressVampy
## Description
I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, especially if I used the same wireless network password as one in the rockyou.txt credential dump.
Use this '[pcap file](https://artifacts.picoctf.net/c/41/wpa-ing_out.pcap)' and the rockyou wordlist. The flag should be entered in the picoCTF{XXXXXX} format.
## Hints
- Finding the IEEE 802.11 wireless protocol used in the wireless traffic packet capture is easier with wireshark, the JAWS of the network.
- Aircrack-ng can make a pcap file catch big air...and crack a password.
## Solution
In this challenge, we were given a .pcap file. I opened it with Wireshark and checked the protocol of the packets. I noticed that it was using `802.11`, which is the standard protocol for Wi-Fi.

The challenge description also mentioned that the password can be found in the rockyou.txt wordlist, and the hint suggested using tools like **aircrack-ng**.

From the packet capture, I found that the Wi-Fi network had the ESSID `Gone-Surfing` and the BSSID `00:5F:67:4F:6A:1A`. You can also confirm this information with the command:
```bash
aircrack-ng wpa-ing_out.pcap
```
Since we need the rockyou.txt file, you can either use the local copy or download it from the internet. To locate it on your system, run:
```bash
find / -name "rockyou.txt"
```
Finally, to perform the brute-force attack against the captured handshake using rockyou.txt, run:
```bash
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b <BSSID> wpa-ing_out.pcap
```
This will result in the cracked key (the Wi-Fi password). Wrap that key with the format `picoCTF{<key>}` and you’ll have the flag.


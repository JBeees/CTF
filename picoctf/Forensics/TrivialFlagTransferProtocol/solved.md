# TITLE : Trivial Flag Transfer Protocol
## Author : Danny
## Description
Figure out how they moved the [flag](https://mercury.picoctf.net/static/ed308d382ae6bcc37a5ebc701a1cc4f4/tftp.pcapng).
## Hints 
What are some other ways to hide data?
## Solution
I received a pcapng file and opened it in Wireshark. From the packets I noticed traffic using the TFTP protocol that appeared to be transferring files. I exported all TFTP objects via File → Export Objects → TFTP, which gave me these files:
```bash
instructions.txt  picture1.bmp  picture2.bmp  picture3.bmp  plan  program.deb
```
I opened instructions.txt. It contained ROT13-encoded text; after decoding it read:
```
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
```
Because the decoded text referenced a “plan,” I opened the plan file. It was also ROT13-encoded; after decoding it read:
```
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```
Next I examined program.deb. It contained information about steganography, which implied that one of the images likely contained hidden data. I attempted a steganography extraction tool on the images, but the tool prompted for a passphrase. The decoded plan mentioned DUEDILIGENCE, so I used that as the passphrase. 
```bash
steghide extract -sf ./picture3.bmp -p "DUEDILIGENCE"
```
Using the passphrase DUEDILIGENCE successfully unlocked hidden data in picture3.bmp. The hidden file was flag.txt. I opened flag.txt and retrieved the flag.


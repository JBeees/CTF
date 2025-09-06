# TITLE : WebNet1
## Author : Jason
## Description
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/fbf98e695555a2a48fe42c9a245de376/picopico.key). Recover the flag. 
## Hints
- Try using a tool like Wireshark.
- How can you decrypt the TLS stream?
## Solution
In this challenge, we were given a .pcap file and a private key, similar to the [WebNet0](https://github.com/JBeees/CTF/tree/main/picoctf/Forensics/WebNet0) challenge. You can review that one first before continuing here. After applying the same process, we can decrypt the traffic and obtain packets that contain files.

Next, we can export these files by going to **File → Export Objects → HTTP** in Wireshark and saving all of them. Among the exported files, there is a .jpg image. Running `exiftool` on this image reveals that the flag is stored in the Artist field of the metadata.

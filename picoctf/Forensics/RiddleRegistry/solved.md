# TITLE : Riddle Registry
## Author : Prince Niyonshuti N.
## Description
Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.
Find the PDF file here [Hidden Confidential Document](https://challenge-files.picoctf.net/c_amiable_citadel/9eb01e29bada8f3c16abe23682c2df28e91a5f9904e505f007e017cc5fb24593/confidential.pdf) and uncover the flag within the metadata.
## Hints
- Don't be fooled by the visible text; it’s just a decoy!
- Look beyond the surface for hidden clues
## Solution
In this challenge, we were given a PDF file. When I opened it, there was no visible information about the flag. After reading the challenge description, it mentioned something about metadata. So I checked the file’s metadata using the command:
```
exiftool <pdf_name>
```
In the metadata output, I noticed a Base64-encoded string in the Author field. After decoding that string, I obtained the flag.

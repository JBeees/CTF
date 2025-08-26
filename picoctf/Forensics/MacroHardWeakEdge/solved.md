# TITLE : MacroHard WeakEdge
## Author : madStacks
## Description
I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/d3dd8cd51524d9fafcccd1b7d55f85e7/Forensics%20is%20fun.pptm)
## Solution
In this challenge, we were given a .pptm file. A .pptm file is a PowerPoint Macro-Enabled Presentation, typically used to include automated tasks such as running calculations, custom slide transitions, buttons that trigger actions, or other programming logic. Internally, .pptm files are actually ZIP archives.

To analyze it, I first unzipped the file with the following commands:
```
cp "Forensics is fun.pptm" copy.pptm
mv copy.pptm copy.zip
unzip copy.zip -d pptm_contents
```
After extracting the contents, I traversed the directory structure and discovered a file named **hidden** that contained base64-encoded data. I decoded the base64 content, and this revealed the flag.

# TITLE : Mob psycho
## Author : NGIRIMANA Schadrack
## Description
Can you handle APKs?
Download the android apk [here](https://artifacts.picoctf.net/c_titan/51/mobpsycho.apk).
## Hints
- Did you know you can unzip APK files?
- Now you have the whole host of shell tools for searching these files.
## Solution
During this challenge, we were given an APK file. I began by extracting its contents using:
```
unzip <apk_name>
```
After unzipping, I explored the extracted directory structure. Since APKs can hide assets or data inside their resource folders, I suspected that the flag might be embedded somewhere within the file tree. To verify this, I recursively listed all files and searched for anything containing the keyword “flag”:
```
find . | grep flag
```
This revealed a file located at:
```
./res/color/flag.txt
```
I opened the file and found that its contents were encoded in hexadecimal. After decoding the hex string, I successfully recovered the flag:
```
7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f35326135653264657d
```


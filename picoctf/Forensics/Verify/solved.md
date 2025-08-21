# TITLE : Verify
## Author : Jeffery John
## Description
People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.
ssh -p 58107 ctf-player@rhea.picoctf.net
Using the password 6abf4a82. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!
- Checksum: b09c99c555e2b39a7e97849181e8996bc6a62501f0149c32447d8e65e205d6d2
- To decrypt the file once you've verified the hash, run ./decrypt.sh files/<file>.
## Hints
- Checksums let you tell if a file is complete and from the original distributor. If the hash doesn't match, it's a different file.
- You can create a SHA checksum of a file with sha256sum <file> or all files in a directory with sha256sum <directory>/.
- Remember you can pipe the output of one command to another with |. Try practicing with the 'First Grep' challenge if you're stuck!
## Solution
To solve this challenge, log in via SSH and run the provided decrypt.sh script on all files inside the files directory. Each file must be processed individually. You can use a simple loop in Bash to do this quickly:
```
for f in files/*; do
    ./decrypt.sh "$f"
done
```
After decrypting all the files, you will obtain the flag.

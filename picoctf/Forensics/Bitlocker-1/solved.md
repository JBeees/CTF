# TITLE : Bitlocker-1
## Author : Venax
## Description
Jacky is not very knowledgable about the best security passwords and used a simple password to encrypt their BitLocker drive. See if you can break through the encryption!
Download the disk image here
## Hints
- Hash cracking
## Solution
In this challenge, we received a disk image. Since the hint mentioned hash cracking, I tried to extract the BitLocker hash from the image. I used the following command:
```
bitlocker2john -i bitlocker-1.dd > hash.txt
```
Inside hash.txt, I found the BitLocker metadata hash, which looked like this:
```
User Password hash:
$bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d
```
This is the user password hash extracted from the BitLocker volume. If we can crack this hash, we can unlock the encrypted drive.

I then used Hashcat with the rockyou.txt wordlist. I copied only the user password hash into a new file called hash3.txt and ran:
```
hashcat -m 22100 hash3.txt /usr/share/wordlists/rockyou.txt
```
Hashcat successfully cracked the password, and the result was:
```
jacqueline
```
Next, I used this password to decrypt the BitLocker volume and mounted it using Dislocker:
```
dislocker -V bitlocker-1.dd -u"jacqueline" -- disk
```
Inside the disk directory, Dislocker generated a file called dislocker-file, which represents the decrypted NTFS volume.
To enumerate the files inside it, I used SleuthKit:
```
fls -r dislocker-file
```
Among the results, I found a file named flag.txt at inode 38-128-1:
```
r/r 38-128-1: flag.txt
```
I then extracted the contents of the file using:
```
icat dislocker-file 38-128-1
```
This command displayed the flag.

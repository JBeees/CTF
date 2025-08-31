# TITLE : DISKO 2
## Author : Darkraicg492
## Description
Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone!
Download the disk image [here](https://artifacts.picoctf.net/c/539/disko-2.dd.gz).
## Hints
How can you extract/isolate a partition?
## Solution
In this challenge, we were given an image file. First, I unzipped the file using `gunzip`. For the .dd file, I used strings to extract possible flags with the following command:
```bash
strings disko-2.dd | grep -o 'picoCTF{4_P4Rt_1t_i5_[^}]*}' > payload.txt
```
This produced many flags with different IDs, which I stored in payload.txt. Since I didn’t know which one was correct, I planned to try all of them until I found the correct one.

First, I submitted a random flag on the challenge page. Then, I opened the developer tools, went to the Network tab, and looked for the POST request named `submissions`. I copied that request as a cURL command.

Next, I ran a loop to submit all the flags from payload.txt:
```bash
while IFS= read -r FLAG; do
    # Paste your copied cURL command here, replacing the flag value with $FLAG
done < payload.txt
```
Finally, I checked the responses and looked for the one where the **correct** field was true. I copied the flag value from that response and that was the correct solution.

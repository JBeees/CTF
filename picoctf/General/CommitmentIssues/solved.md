# TITLE : Commitment Issues
## Author : Jeffery John
## Description
I accidentally wrote the flag down. Good thing I deleted it!
You download the challenge files here:
[challenge.zip](https://artifacts.picoctf.net/c_titan/75/challenge.zip)
## Hints
- Version control can help you recover files if you change or lose them!
- Read the chapter on Git from the picoPrimer here
- You can 'checkout' commits to see the files inside them
## Solution
In this challenge, we were given a ZIP file. After extracting it, I ran `ls -a` to inspect the directory contents. Inside, I found a `message.txt` file and a `.git` directory.

When I opened `message.txt`, it only contained the text `TOP SECRET`, which was obviously not the real flag. So I decided to investigate the `.git` folder, since it often contains leftover history.
I went into `.git/logs/` and checked the `HEAD` file. The logs showed the following:
```
0000000000000000000000000000000000000000 6603cb4ff0c4ea293798c03a32e0d78d5ab12ca2 picoCTF <ops@picoctf.com> 1710018598 +0000	commit (initial): create flag
6603cb4ff0c4ea293798c03a32e0d78d5ab12ca2 3899edb7f3110d613c72ad40083fd8feeef703d0 picoCTF <ops@picoctf.com> 1710018598 +0000	commit: remove sensitive info
```
This tells us two things:
1. The first commit created the flag.    
2. The next commit removed the sensitive information.   
So the flag still exists in the initial commit, even though it was later deleted.
To recover it, I simply checked out the first commit:
```
git checkout 6603cb4ff0c4ea293798c03a32e0d78d5ab12ca2
```
After switching to that commit, I opened `message.txt` again — and there was the full flag.

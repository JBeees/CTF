# TITLE : Time Machine
## Author : Jeffery John
## Description
What was I last working on? I remember writing a note to help me remember...
You can download the challenge files here:
[challenge.zip](https://artifacts.picoctf.net/c_titan/66/challenge.zip)
## Hints
- The cat command will let you read a file, but that won't help you here!
- Read the chapter on Git from the picoPrimer here.
- When committing a file with git, a message can (and should) be included.
## Solution
In this challenge, we were given a ZIP file. I started by unzipping it using the `unzip` command. Inside, there was a file called `message.txt` containing the following note:
```
This is what I was working on, but I'd need to look at my commit history to know why...
```
The problem hinted that we should check the Git history. So, I ran `ls -a` and found a `.git` directory. Inside it, I navigated to the `logs` directory and found a file named `HEAD`. After viewing its contents, I discovered the flag there.

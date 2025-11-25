# TITLE : Collaborative Development
## Author : Jeffery John
## Description
My team has been working very hard on new features for our flag printing program! I wonder how they'll work together?
You can download the challenge files here:
[challenge.zip](https://artifacts.picoctf.net/c_titan/69/challenge.zip).
## Hints
- git branch -a will let you see available branches
- How can file 'diffs' be brought to the main branch? Don't forget to git config!
- Merge conflicts can be tricky! Try a text editor like nano, emacs, or vim.
## Solution
In this challenge, we were given a ZIP file. After extracting it, I ran `ls -a` and noticed two important items inside the directory: `flag.py` and a `.git` folder. Since the `.git` directory often contains useful metadata, I explored it and checked the contents of the `HEAD` log located in `.git/logs/HEAD`.

The log revealed a series of branch checkouts and commits. Each commit message indicated that a different “part” of the flag had been added on separate branches. The history looked like this (shortened):
- Initial commit: added the flag printer
- Switched from main to feature/part-1, then committed “part 1”
- Switched back to main
- Moved to feature/part-2, committed “part 2”
- Returned to main
- Moved to feature/part-3, committed “part 3”
This strongly suggested that each branch contained a different segment of the flag.
To retrieve the differences, I compared each feature branch against the main branch using:
```
git diff main..feature/part-1
git diff main..feature/part-2
git diff main..feature/part-3
```
Each diff revealed a separate portion of the flag. After extracting all three segments and combining them, I obtained the complete flag.

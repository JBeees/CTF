# TITLE : credstuff
## Author : Will Hong / LT 'syreal' Jones
## Description
We found a leak of a blackmarket website's login credentials. Can you find the password of the user cultiris and successfully decrypt it?
Download the leak here.
The first user in usernames.txt corresponds to the first password in passwords.txt. The second user corresponds to the second password, and so on.
- Maybe other passwords will have hints about the leak?
## Solution
To solve this challenge, you need to find the line where `cultiris` appears in the `usernames.txt` file. Then, retrieve the password on the same line. You can use the `grep` command to help you locate the line:
```bash
grep -n cultiris usernames.txt
```
After finding the password, note that it is encoded using ROT13. You must decode it to get the actual password.

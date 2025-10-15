# TITLE : Super SSH
## Author : Jeffery John
## Description
Using a Secure Shell (SSH) is going to be pretty important.
Additional details will be available after launching your challenge instance.
## Hints
- https://linux.die.net/man/1/ssh
- You can try logging in 'as' someone with <user>@titan.picoctf.net
- How could you specify the port?
- Remember, passwords are hidden when typed into the shell
## Solution
In this challenge, we only need to connect to the SSH service to get the flag using:
```bash
ssh <user>@<host> -p <port>
```

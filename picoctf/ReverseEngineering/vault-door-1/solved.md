# TITLE : vault-door-1
## Author : Mark E. Haase
## Description
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/ff2585f7afd21b81f69d2fbe37c081ae/VaultDoor1.java)
## Hints
- Look up the charAt() method online.
## Solution
We were given a Java function checkPassword(String password). The function validates the input by checking whether specific characters appear at fixed positions within the password. To solve the challenge, we needed to reconstruct the password **flag** directly from the conditions in the function.

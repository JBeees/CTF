# TITLE : vault-door-training
## Author : Mark E. Haase
## Description
Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://jupiter.challenges.picoctf.org/static/03c960ddcc761e6f7d1722d8e6212db3/VaultDoorTraining.java)

## Hints 
- The password is revealed in the program's source code.

## Solution 
As hinted, the password is hardcoded in the source code, specifically within the checkPassword function. To obtain the flag, simply extract the password from that function and wrap it in the format `picoCTF{...}`.
## Flag
<pre>picoCTF{w4rm1ng_Up_w1tH_jAv4_3808d338b46}</pre>

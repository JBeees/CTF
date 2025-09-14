# TITLE : vault-door-3
## Author : Mark E. Haase
## Description
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a648ca6dd275b9454c5d0de6d0f6efd3/VaultDoor3.java)
## Hints 
- Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.
## Solution
In this challenge we were given a Java file about an anagram problem. We had to supply the correct flag so that, after the program’s reordering (anagram) logic, it produced the string `jU5t_a_sna_3lpm18gb41_u_4_mfr340`. I submitted
`picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}`
and the program accepted it.

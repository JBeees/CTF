# TITLE : vault-door-7
## Author : Mark E. Haase
## Description
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: [VaultDoor7.java](https://jupiter.challenges.picoctf.org/static/89b8065d19ee9830ae548d27a40ca757/VaultDoor7.java)
## Hints
- Use a decimal/hexadecimal converter such as this one: https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html
- You will also need to consult an ASCII table such as this one: https://www.asciitable.com/
## Solution
In this challenge, we were given a Java file. When I read the code, I realized that the program converts a string into bytes and then performs bit shifts on each group of four characters. You can see this logic in the following function:
```java
public int[] passwordToIntArray(String hex) {
        int[] x = new int[8];
        byte[] hexBytes = hex.getBytes();
        for (int i=0; i<8; i++) {
            x[i] = hexBytes[i*4]   << 24
                 | hexBytes[i*4+1] << 16
                 | hexBytes[i*4+2] << 8
                 | hexBytes[i*4+3];
        }
        return x;
}
```
Then, in the `checkPassword` function, it verifies whether the converted integers match the correct values:
```java
return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734291511
            && x[6] == 960049251
            && x[7] == 1681089078;
```
So, I simply reversed the encoding process to get the original string — and that revealed the flag.

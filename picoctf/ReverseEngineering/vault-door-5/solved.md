# TITLE : vault-door-5
## Author : Mark E. Haase
## Description
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](https://jupiter.challenges.picoctf.org/static/9505cca05dc00fecead41106370ee619/VaultDoor5.java)
## Hints 
- You may find an encoder/decoder tool helpful, such as https://encoding.tools/
- Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.
## Solution
In this challenge, we were given a Java file containing a `checkPassword` function. To get the flag, the program uses an expected `variable`, which is **Base64-encoded**:
```java
String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTM4JTM0JTY2JTY0JTM1JTMwJTM5JTM1";
```
first **Base64-decoded** this string and obtained a percent-encoded (URL-encoded) string:
```
%63%30%6e%76%33%72%74%31%6e%67%5f%66%72%30%6d%5f%62%61%35%65%5f%36%34%5f%38%34%66%64%35%30%39%35
```
Next, I percent-decoded this value to get the final flag.

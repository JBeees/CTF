# TITLE : Fresh Java 
## Author : LT 'syreal' Jones
## Description
Can you get the flag?
Reverse engineer this [Java program](https://artifacts.picoctf.net/c/197/KeygenMe.class).
## Hints
- Use a decompiler for Java!
## Solution
In this challenge we were given a Java `.class` file. To get the flag I decompiled it with [JD-GUI](https://java-decompiler.github.io/) and obtained the full Java source. After reversing the code and reading the checks, I reconstructed the flag and submitted it successfully.

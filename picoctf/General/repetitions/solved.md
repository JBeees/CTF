# TITLE : repetitions
## Author : Theoneste Byagutangaza
## Description
Can you make sense of this file?
Download the file [here](https://artifacts.picoctf.net/c/471/enc_flag).
## Hints
- Multiple decoding is always good.
## Solution
In this challenge, we were given an `enc_flag` file, and the hint mentioned multiple layers of decoding. When I checked the content, it looked like Base64-encoded text:
```
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVhRmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNkMlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVWVkpEVGxaYVdFMVhSbFpSV0VKWVZGVmtNRTVHV2tWU2JYUlVDbUpXV25sVWJGcHZWbGRHZEdWRlZsaGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```
Since it appeared to be Base64, I decoded it multiple times using the `base64` command. After several rounds of decoding, I finally obtained the flag.

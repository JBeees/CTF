# TITLE : RED
## Author : Shuailin Pan (LeConjuror)
## Description
RED, RED, RED, RED
Download the image: [red.png](https://challenge-files.picoctf.net/c_verbal_sleep/831307718b34193b288dde31e557484876fb84978b5818e2627e453a54aa9ba6/red.png)
## Hints
- The picture seems pure, but is it though?
- Red?Ged?Bed?Aed?
- Check whatever Facebook is called now.
## Solution
In this challenge, I used the tool zsteg to extract hidden information from the image. After running the command, I obtained an encoded Base64 string. I then decoded it and successfully retrieved the flag.
```
zsteg <image name>
``` 

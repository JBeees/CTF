# TITLE : Glory Of The Garden
## Author : jedavis/Danny
## Description
This [garden](https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg) contains more than it seems.
## Hints
- What is a hex editor?
## Solution
In this challenge, we only need to look at the hex representation of the image. By using a tool called xxd, we can view the file contents in hexadecimal format. Inside the hex output, the flag is visible.
Here is the xxd command:  
```
xxd <image_name>
```

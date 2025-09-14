# TITLE : speeds and feeds
## Author : Ryan Ramseyer
## Description
There is something on my shop network running at nc mercury.picoctf.net 16524, but I can't tell what it is. Can you?
## Hints 
- What language does a CNC machine use?
## Solution
In this challenge we were given a network capture delivered via netcat. When I ran it, the output contained text I didn’t recognize at first. After investigating, I discovered the output was **G-code** — the control language used by CNC machines.

To view and interpret the **G-code**, I used the web tool [**ncviewer**](https://ncviewer.com/). I copied the content produced by the netcat session into ncviewer, which rendered the toolpath. From that visualization I was able to read the encoded output and retrieve the flag.

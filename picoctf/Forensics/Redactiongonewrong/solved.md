# TITLE : Redaction gone wrong
## Author : Mubarak Mikail
## Description
Now you DON’T see me.  

This [report](https://artifacts.picoctf.net/c/84/Financial_Report_for_ABC_Labs.pdf) has some critical data in it, some of which have been redacted correctly, while some were not. Can you find an important key that was not redacted properly?
## Hints
- How can you be sure of the redaction?
## Solution
In this challenge, we are given a .pdf file. When opening the file, there are blacked-out areas that appear to cover some text. However, the text isn’t truly removed — it’s only visually hidden.

To extract the actual content, I used the pdftotext tool with the following command:
```
pdftotext Financial_Report_for_ABC_Labs.pdf output.txt
```
After checking the generated output.txt file, the hidden text is revealed, and from there you can obtain the flag.


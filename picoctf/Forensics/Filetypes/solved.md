# TITLE : File types
## Author : Geoffrey Njogu
## Description
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.
You can download the file from [here](https://artifacts.picoctf.net/c/80/Flag.pdf).
## Hints
- Remember that some file types can contain and nest other files
## Solution
In this challenge, the file initially appears to be a PDF, but its actual content is a shell archive (shar) that contains a file named flag. After identifying this, I renamed the file with a .sh extension and executed it:
```
./<file_name>.sh
```
Running the script extracts a file named flag, which turns out to be an archive container, not the actual flag. Further inspection shows that the file is first an ar archive, and after extraction, it becomes a cpio archive.

From there, the challenge requires repeatedly identifying and decompressing the file using the correct tools based on its detected format. The file is wrapped in multiple compression layers, including:
- bzip2
- gzip
- lzip
- lz4
- lzma / xz
- lzop
After each decompression step, the file must be checked again using tools like file to determine the next required decompression method.

Eventually, the final output is an ASCII text file containing data encoded in hexadecimal format. Decoding this hex data reveals the actual flag.

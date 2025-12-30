# TITLE :  Exif
## Description
If only the password were in the image?

https://mega.nz/#!SDpF0aYC!fkkhBJuBBtBKGsLTDiF2NuLihP2WRd97Iynd3PhWqRw You could really ‘own’ it with exif.
## Solution
In this challenge, we were given a JPG file. Since the challenge referenced metadata, I analyzed the image using exiftool. Within the metadata, I found the flag stored in the `Owner Name` field. After wrapping it in the CTFlearn{...} format, the submission was accepted.

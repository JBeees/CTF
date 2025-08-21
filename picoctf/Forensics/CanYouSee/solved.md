# TITLE : CanYouSee
## Author : Mubarak Mikail
## Description
How about some hide and seek?
Download this file [here](https://artifacts.picoctf.net/c_titan/131/unknown.zip).
## Hints
- How can you view the information about the picture?
- If something isn't in the expected form, maybe it deserves attention?
## Solution
In this challenge, you only need to unzip the .zip file and check the metadata of the extracted image. You can use a tool called [**exiftool**](https://exiftool.org/) to view the metadata. Look at the Attribution URL field, which contains a string encoded in Base64. After decoding it, you will get the flag.

Here is the exiftool command:
```
exiftool <image_name>
```

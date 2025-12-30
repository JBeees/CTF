# TITLE : 07601
## Author : alexkato29
## Description
ttps://mega.nz/#!CXYXBQAK!6eLJSXvAfGnemqWpNbLQtOHBvtkCzA7-zycVjhHPYQQ I think I lost my flag in there. Hopefully, it won't get attacked...
## Solution 
In this challenge, we were given a JPG file. While inspecting the file using `xxd`, I noticed suspicious data, which suggested the presence of embedded content. I then used `binwalk -e <file_name>` to extract the embedded files. From the extracted results, I found another image. Running the `strings` command on this image revealed the flag wrapped in `ABCDE{...}`. After submitting it in the `CTFlearn{...}` format, the flag was accepted.

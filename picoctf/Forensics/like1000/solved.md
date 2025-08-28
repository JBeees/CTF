# TITLE : like1000
## Author : DANNY
## Description
This [.tar file](https://jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar) got tarred a lot.
## Hints
- Try and script this, it'll save you a lot of time
## Solution
In this challenge, I was given a .tar file. When extracting it, the archive produced another .tar file along with a filler.txt file. After some testing, I discovered that this process repeats about 1000 times.

Extracting each file manually would be impractical, so I wrote a Bash script to automate the process. The script repeatedly extracts the current .tar file, prints the contents of any .txt files, and then proceeds to the next .tar file.

Here is the script I used:
```bash
#!/bin/bash
file="1000.tar"

while true; do
    tar -xvf "$file" || break
    
    # If a .txt file is present, print its content
    if ls *.txt 1> /dev/null 2>&1; then
        for txt in *.txt; do
            echo "==== Found $txt ===="
            cat "$txt"
        done
    fi

    # Find the next .tar file
    next=$(ls *.tar 2>/dev/null | sort -n | head -1)
    if [ -z "$next" ] || [ "$next" == "$file" ]; then
        break
    fi
    file="$next"
done
```
After the final extraction, the last archive contained a .png image. Opening the image revealed the flag. ✅

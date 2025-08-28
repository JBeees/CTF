#!/bin/bash
file="1000.tar"

while true; do
    tar -xvf "$file" || break
    
    # if a .txt file shows up, print its content
    if ls *.txt 1> /dev/null 2>&1; then
        for txt in *.txt; do
            echo "==== Found $txt ===="
            cat "$txt"
        done
    fi

    # find the next .tar file
    next=$(ls *.tar 2>/dev/null | sort -n | head -1)
    if [ -z "$next" ] || [ "$next" == "$file" ]; then
        break
    fi
    file="$next"
done


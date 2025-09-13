# TITLE : file-run2
## Author : Will Hong
## Description
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"?
Download the program here.
## Hints 
- Try running it and add the phrase "Hello!" with a space in front (i.e. "./run Hello!")
## Solution
We were given a binary file but didn't have permission to run it. To make it executable, run:`chmod +x run`. Then execute the program with the argument Hello!:`./run Hello!` The program will print the flag.

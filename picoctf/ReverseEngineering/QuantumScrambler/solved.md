# TITLE : Quantum Scrambler
## Author : Michael Crotty
## Description
We invented a new cypher that uses "quantum entanglement" to encode the flag. Do you have what it takes to decode it?
Connect to the program with netcat:
$ nc verbal-sleep.picoctf.net 49307
The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_verbal_sleep/2d5f628b924b261f88e22f693ad13574a015c58f6006c9d3b15daee312162feb/quantum_scrambler.py).
## Hints
- Run eval on the cypher to interpret it as a python object
- Print the outer list one object per line
- Print the outer list one object per line
## Solution
In this challenge we have a Python program that scrambles our flag and prints the scrambled output. For testing I inserted a value like `flag` and got an output like:
```bash
[['0x66', '0x6c'], ['0x61', []], ['0x67']]
```
I discovered the program encodes the flag by placing meaningful bytes in the first and last positions of each sublist. I retrieved the full scrambled output (for example via `nc`) and saved it to `input.txt`. I then ran a script to extract the first and last items from each line and decode them to recover the flag.
```py
with open("input.txt") as f:
    content = f.read().strip()

##print(content)
res = eval(content)
for line in res:
    if isinstance(line, list) and line:   # make sure it's a non-empty list
        first = line[0]
        last = line[-1]
        print("first:", first, " last:", last)
```

# TITLE : SideChannel
## Author : Anish Singhani
## Description
There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?
Download the PIN checker program here [pin_checker](https://artifacts.picoctf.net/c/73/pin_checker)
## Hints
- Read about "timing-based side-channel attacks."
- Attempting to reverse-engineer or exploit the binary won't help you, you can figure out the PIN just by interacting with it and measuring certain properties about it.
- Don't run your attacks against the master server, it is secured against them. The PIN code you get from the pin_checker binary is the same as the one for the master server.
## Solution
In this challenge, we are given an executable file. When executed, the program prompts the user to enter an 8-digit PIN.

I first inspected the file using the file command:
```
file <file_name>
```
The output showed that the binary is stripped, which means symbol information has been removed, making static reverse engineering more difficult.

After reading the challenge hint, it became clear that the intended solution involved a timing-based side-channel attack. A **timing-based side-channel attack** is an attack technique where an attacker infers secret information by measuring how long a system takes to perform an operation, rather than exploiting a direct vulnerability in the code.

To validate this, I performed several manual tests by providing different PIN inputs and measuring the execution time. I observed that inputs with a longer correct prefix caused the program to take slightly more time to respond. This indicates that the program likely compares the PIN character by character and exits early when a mismatch occurs, which introduces a timing leak.

Based on this observation, I implemented a brute-force timing attack. The idea is to determine the PIN one digit at a time by selecting the digit that results in the maximum execution time, which suggests that more characters were correctly matched.

The script below automates this process:
```py
import time
import subprocess 

def test_pin(pin):
  start_time = time.time()
  result= subprocess.run(["./pin_checker"], input=pin.encode(), capture_output=True)
  end_time   = time.time()
  return  end_time - start_time

max_time = 0
index = 0
correct_pin = ""
for i in range(8):
    for j in range(0,10):
        testpin = correct_pin + str(j) + (str(j) * (7 - i))
        cur_time =  test_pin(testpin)
        print("Test PIN : ",testpin)
        if (cur_time > max_time):
            max_time = cur_time
            index = j
    correct_pin = correct_pin + str(index)
    max_time = 0
    print(correct_pin)
```
Using this script, I successfully recovered the correct PIN locally. I then reused the same PIN on the remote server, which resulted in the program accepting the input and returning the   flag.

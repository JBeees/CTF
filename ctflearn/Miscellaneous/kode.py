from pwn import *
import random

HOST = "138.197.193.132"
PORT = 5001

io = remote(HOST, PORT)

# Step 1: send a dummy move for the first round
io.recvuntil(b">>>")
io.sendline(b"R")
while True:
    print(rand())
    line = io.recvline().decode().strip()
    print(line)
    
    if "based on" in line:
        number = int(line.split()[-1])
        mod = number % 3

        # Predict server's NEXT move
        if mod == 0:      # R
            move = "P"
        elif mod == 1:    # P
            move = "S"
        else:             # S
            move = "R"

        io.recvuntil(b">>>")
        io.sendline(move.encode())


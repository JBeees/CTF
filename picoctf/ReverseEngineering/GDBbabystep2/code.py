four = 0x1e0da
c = 0x25f
eight = 0x0
eax = 0x0
while eax < c:
    eax = eight
    four += eax
    eight += 0x1
    eax = eight
eax = four
print("eax", eax)

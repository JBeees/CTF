with open("whitepages.txt", "r", encoding="utf-8") as f:
    data = f.read()

binary = ""
for ch in data:
    if ch == " ":         # normal space
        binary += "1"
    elif ch == "\u2003":  # EM SPACE
        binary += "0"

# split into bytes
message = "".join(
    chr(int(binary[i:i+8], 2))
    for i in range(0, len(binary), 8)
)

print(message)


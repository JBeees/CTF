with open("TheMessage.txt", "r", encoding="utf-8") as f:
    data = f.read()

binary = ""
for ch in data:
    if ch == " ":         # normal space
        binary += "0"
    elif ch == "\u200f":  # EM SPACE
        binary += "1"

# split into bytes
message = "".join(
    chr(int(binary[i:i+8], 2))
    for i in range(0, len(binary), 8)
)

print(message)


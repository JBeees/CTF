numbers = [165, 248, 94, 346, 299, 73, 198, 221, 313, 137, 205, 87, 336, 110, 186, 69, 223, 213, 216, 216, 177, 138]
flag = ""

for n in numbers:
    temp = n % 37
    if 0 <= temp <= 25:       # 0-25 → A-Z
        flag += chr(65 + temp)
    elif 26 <= temp <= 35:    # 26-35 → 0-9
        flag += str(temp - 26)
    elif temp == 36:          # 36 → _
        flag += '_'

print(flag)


def ascii_decrement(s: str) -> str:
    result = []
    i = 0
    for c in s:
        if i % 2 == 0:
            result.append(chr(ord(c) + 1))
        else :
            result.append(chr(ord(c) - 1))
        i+=1
    return ''.join(result)


# Example usage
text = "BUGMd`sozc0o`sx^0r^`vdr1ld|"
print(text)
decoded = ascii_decrement(text)
print(decoded)


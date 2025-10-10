#!/usr/bin/env python3
# decode_sub5.py
# Subtract 0x05 from each hex byte and print hex + ASCII result.
# Usage:
#   python decode_sub5.py "4b 80 6b 35 7a 73 69 64 36 71"
# or
#   echo "4b 80 6b 35 ..." | python decode_sub5.py

import sys

def decode_sub5(hex_bytes):
    out_bytes = []
    for h in hex_bytes:
        # allow "0x.." or plain hex
        if h.startswith("0x") or h.startswith("0X"):
            val = int(h, 16)
        else:
            val = int(h, 16)
        new = (val - 0x05) & 0xFF
        out_bytes.append(new)
    return bytes(out_bytes)

def main():
    if not sys.stdin.isatty():
        data = sys.stdin.read().strip()
    elif len(sys.argv) > 1:
        data = " ".join(sys.argv[1:])
    else:
        print("Usage: decode_sub5.py \"4b 80 6b ...\"  or pipe the hex string in.")
        sys.exit(1)

    # split on whitespace, commas, or newlines
    parts = [p for p in data.replace(",", " ").split() if p]
    try:
        decoded = decode_sub5(parts)
    except ValueError as e:
        print("Error parsing hex bytes:", e)
        sys.exit(2)

    # print hex
    print("Decoded hex:", " ".join(f"{b:02x}" for b in decoded))
    # try ascii (replace non-printable with dot)
    ascii_out = "".join((chr(b) if 32 <= b <= 126 else ".") for b in decoded)
    print("ASCII      :", ascii_out)

if __name__ == "__main__":
    main()


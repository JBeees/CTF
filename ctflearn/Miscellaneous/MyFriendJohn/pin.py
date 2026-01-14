def generate_pins(filename: str):
    with open(filename, "w") as f:
        # 4-digit PINs: 0000–9999
        for i in range(10000):
            f.write(f"{i:04d}\n")

        # 6-digit PINs: 000000–999999
        for i in range(1000000):
            f.write(f"{i:06d}\n")


generate_pins("pins.txt")

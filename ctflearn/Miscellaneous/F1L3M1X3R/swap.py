def transform_image(input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()

    transformed = bytearray()

    # Process in 4-byte chunks
    for i in range(0, len(data), 4):
        chunk = data[i:i+4]

        # If chunk is smaller than 4 bytes, keep it as-is
        if len(chunk) < 4:
            transformed.extend(chunk)
            continue

        block1 = chunk[:2]
        block2 = chunk[2:]

        # Swap blocks and reverse bytes in each block
        transformed.extend(block2[::-1] + block1[::-1])

    with open(output_file, "wb") as f:
        f.write(transformed)

    print("Transformation completed successfully.")

# Example usage
transform_image("fl4g.jpeg", "output.jpg")


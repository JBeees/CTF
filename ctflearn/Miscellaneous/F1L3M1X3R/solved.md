# TITLE : FIL3 M1X3R
## Author : RedK
## Description
I think my amazing photo was hit by a mixer and now it is not working. Help me fix it? https://mega.nz/#!Ds0mWaCJ!4uKfJeJwhupG7Tvx8ReTBP1reFgdzRLE3YrN0l-5Jrg hint: visit: https://en.wikipedia.org/wiki/List_of_file_signatures Programming might be useful in this challenge
## Solution
In this challenge, we were given a corrupted JPEG file. I began by inspecting the file’s raw bytes using xxd to view its hexadecimal representation. From this analysis, I observed that the bytes were swapped and reversed in pairs throughout the file.

For example, instead of a valid JPEG header such as:
```
ffd8 ffe0
```
the file contained:
```
e0ff d8ff
```
This indicated that, for every 4 bytes, the data had been transformed by:
1. Splitting the bytes into two 2-byte blocks    
2. Swapping the two blocks    
3. Reversing the byte order within each block    
To recover the original file, this transformation had to be applied to the entire image, not just the header.

I implemented the following Python script to perform this operation on all bytes in the file:
```
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
```
After running this script, I opened the resulting image file. The JPEG was successfully restored, and the flag was visible in the image.

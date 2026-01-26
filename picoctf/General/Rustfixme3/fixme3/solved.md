# TITLE : Rust fixme 3
## Author : Taylor McCampbell
## Description
Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!
Download the Rust code [here](https://challenge-files.picoctf.net/c_verbal_sleep/dcdaf491b35c1d0f5075e9583edbbb7aaea1dffb6ad32bc000e4d87b5200ff7b/fixme3.tar.gz).
## Hints
- Read the comments...darn it!
## Solution
In this challenge, we were provided with a `.tar.gz` file. The first step was to extract the archive using the following command:
```
tar -xzf file.tar.gz
```
After extracting the files, I examined the Rust source code. The challenge focused on unsafe operations in Rust, specifically how Rust handles low-level memory access.

I identified the following line of code:
```rust
let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);
```
This line calls std::slice::from_raw_parts, which is an unsafe function. Rust marks this function as unsafe because the compiler cannot verify that the raw pointer and length are valid, properly aligned, and point to initialized memory. As a result, the call must be explicitly wrapped in an unsafe block to acknowledge the associated risks.

To fix the issue, I modified the code as follows:
```rust
let decrypted_slice = unsafe {
    std::slice::from_raw_parts(decrypted_ptr, decrypted_len)
};
```

By doing this, I explicitly accepted responsibility for ensuring that the pointer and length were valid.

After applying this change, I recompiled and ran the program using: `cargo run`. The program executed successfully and printed the flag, completing the challenge.


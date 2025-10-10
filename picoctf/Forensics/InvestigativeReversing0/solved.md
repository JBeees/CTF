# TITLE : Investigative Reversing 0
## Author : Danny Tunitis
## Description
We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/6e007dc305ebb3d94c2ab361ee0127a6/mystery) and an [image](https://jupiter.challenges.picoctf.org/static/6e007dc305ebb3d94c2ab361ee0127a6/mystery.png). See what you can make of it. There should be a flag somewhere.
## Hints
- Try using some forensics skills on the image
- This problem requires both forensics and reversing skills
- A hex editor may be helpful
## Solution
In this challenge we were given a single binary and one image. I opened the binary in Ghidra and found the following main function:
```c
void main(void)

{
  FILE *flag_file;
  FILE *image;
  size_t sVar1;
  long in_FS_OFFSET;
  int local_54;
  int local_50;
  char flag_content [4];
  char local_34;
  char local_33;
  char local_29;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  flag_file = fopen("flag.txt","r");
  image = fopen("mystery.png","a");
  if (flag_file == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (image == (FILE *)0x0) {
    puts("mystery.png is missing, please run this on the server");
  }
  sVar1 = fread(flag_content,0x1a,1,flag_file);
  if ((int)sVar1 < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("at insert");
  fputc((int)flag_content[0],image);
  fputc((int)flag_content[1],image);
  fputc((int)flag_content[2],image);
  fputc((int)flag_content[3],image);
  fputc((int)local_34,image);
  fputc((int)local_33,image);
  for (local_54 = 6; local_54 < 0xf; local_54 = local_54 + 1) {
    fputc((int)(char)(flag_content[local_54] + '\x05'),image);
  }
  fputc((int)(char)(local_29 + -3),image);
  for (local_50 = 0x10; local_50 < 0x1a; local_50 = local_50 + 1) {
    fputc((int)flag_content[local_50],image);
  }
  fclose(image);
  fclose(flag_file);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```
### What this code actually does

* Although `flag_content` is declared as char `flag_content[4]`;, the program calls `fread(flag_content, 0x1a, 1, flag_file)`; which reads 0x1a = 26 bytes starting at flag_content on the stack. This overwrites adjacent local variables, which is why the binary later indexes flag_content well past index 3.

* The program writes bytes into the image in this order:
    1. `flag_content[0..3]`
    2. `local_34`, `local_33` (these are bytes that were filled by the earlier fread because of the overflow)
    3. `flag_content[6..14]`, but each byte is incremented by 0x05 before being written
    4. `local_29 - 3` (again local_29 comes from the fread area)
    5. `flag_content[0x10..0x19]`  (bytes 16..25 from the fread)

* The saved stack-canary check (`local_10 = *(long *)(in_FS_OFFSET + 0x28`); ... `__stack_chk_fail())` prevents the function from silently continuing if the overflow overwritten the canary.

### What I found from the image

I ran **zsteg** on the produced image and extracted this string:
```
picoCTK.k5zsid6q_fb51c821}
```
Using the program logic above (and applying the +0x05 transformation where appropriate, and the -3 on `local_29`), I reconstructed the flag from the bytes written into the image.

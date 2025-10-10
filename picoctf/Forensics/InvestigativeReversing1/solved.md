# TITLE : Investigative Reversing 1
## Author : Danny Tunitis
## Description
We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/92096ac1cf6a683acb886256b58b5020/mystery) and a few images: [image](https://jupiter.challenges.picoctf.org/static/92096ac1cf6a683acb886256b58b5020/mystery.png), [image2](https://jupiter.challenges.picoctf.org/static/92096ac1cf6a683acb886256b58b5020/mystery2.png), [image3](https://jupiter.challenges.picoctf.org/static/92096ac1cf6a683acb886256b58b5020/mystery3.png). See what you can make of it. There should be a flag somewhere.
## Hints
- Try using some forensics skills on the image
- This problem requires both forensics and reversing skills
- A hex editor may be helpful
## Solution
In this challenge we were given a binary and three images. I opened the binary in Ghidra and found the main function shown below:
```c
void main(void)

{
  FILE *flag_file;
  FILE *pic_1;
  FILE *pic_2;
  FILE *pic_3;
  long in_FS_OFFSET;
  char local_6b;
  int local_68;
  int local_64;
  int local_60;
  char flag_content [4];
  char local_34;
  char local_33;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  flag_file = fopen("flag.txt","r");
  pic_1 = fopen("mystery.png","a");
  pic_2 = fopen("mystery2.png","a");
  pic_3 = fopen("mystery3.png","a");
  if (flag_file == (FILE *)0x0) {
     puts("No flag found, please make sure this is run on the server");
  }
  if (pic_1 == (FILE *)0x0) {
     puts("mystery.png is missing, please run this on the server");
  }
  fread(flag_content,0x1a,1,flag_file);
  fputc((int)flag_content[1],pic_3);
  fputc((int)(char)(flag_content[0] + '\x15'),pic_2);
  fputc((int)flag_content[2],pic_3);
  local_6b = flag_content[3];
  fputc((int)local_33,pic_3);
  fputc((int)local_34,pic_1);
  for (local_68 = 6; local_68 < 10; local_68 = local_68 + 1) {
     local_6b = local_6b + '\x01';
     fputc((int)flag_content[local_68],pic_1);
  }
  fputc((int)local_6b,pic_2);
  for (local_64 = 10; local_64 < 0xf; local_64 = local_64 + 1) {
     fputc((int)flag_content[local_64],pic_3);
  }
  for (local_60 = 0xf; local_60 < 0x1a; local_60 = local_60 + 1) {
     fputc((int)flag_content[local_60],pic_1);
  }
  fclose(pic_1);
  fclose(flag_file);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                            /* WARNING: Subroutine does not return */
     __stack_chk_fail();
  }
  return;
}
```
The program’s purpose is to distribute the contents of the flag file across the three images. I ran **zsteg** on all three output images and found:

- Image 1 → CF{An1_e2630725}
- Image 2 → .s
- Image 3 → icT0tha_

Using the `fputc` calls shown in main, I manually reconstructed the flag by following the order and transformations the program uses. Note that image 2 is used: it receives a transformed byte (specifically `flag_content[0] + 0x15`) and also gets `local_6b` later, so its content is relevant to flag reconstruction. Based on the bytes extracted from the images and the program logic, I recovered the full flag.

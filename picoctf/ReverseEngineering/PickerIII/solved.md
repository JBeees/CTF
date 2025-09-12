# TITLE : Picker III
## Author : LT 'syreal' Jones
## Description
Can you figure out how this program works to get the flag?  
Connect to the program with netcat: 
nc saturn.picoctf.net 56708  
The program's source code can be downloaded here.  
## Hints
- Is there any way to modify the function table?
## Solution
We are given a Python script that contains a hidden win() function which prints the flag (as hex). The program does not expose win() directly from its menu, but it keeps a global func_table string containing names of allowed functions in fixed-size slots:
```python
FUNC_TABLE_SIZE = 4
FUNC_TABLE_ENTRY_SIZE = 32
```
So func_table is a single string of 4 × 32 = 128 characters. Each function name is left-aligned in a 32-character slot and padded with spaces. The program extracts the nth function by computing an offset n * 32 and reading characters until the first space — that substring becomes the callable function name. Finally, call_func(n) does eval(func_name + '()'), so if func_name == 'win' it will call win().

The program also provides a write_variable() option that runs an exec like:
```python
exec('global '+var_name+'; '+var_name+' = '+value)
```
The input filter only blocks ;, ( and ), but it allows quoted string literals. That means we can overwrite func_table by supplying a properly quoted 128-character string, placing win into the desired slot.

**Steps to exploit**

Run the program:
```python
python3 picker-III.py
```
Choose the write variable option (menu option 3).
When prompted for variable name, enter:
```bash
func_table
```
When prompted for the new value, paste exactly this single-quoted string (including the outer quotes):
```bash
'print_table                     read_variable                   win                             getRandomNumber                 '
```
Notes:
- This string is 4 slots × 32 chars each = 128 chars.
- Each slot is padded with spaces so alignment remains correct.
- The third slot contains win (padded to 32 chars).

Back at the main menu, enter 3 (to call the 3rd function). Because the third slot now contains win, the program runs win() and prints the flag as space-separated hex bytes.

Convert the hex bytes to ASCII to get the readable flag.

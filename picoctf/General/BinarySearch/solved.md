# TITLE : Binary Search
## Author : Jeffery John
## Description
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.
Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!
You can download the challenge files here:
[challenge.zip](https://artifacts.picoctf.net/c_atlas/4/challenge.zip)
## Hints
- Have you ever played hot or cold? Binary search is a bit like that.
- You have a very limited number of guesses. Try larger jumps between numbers!
- The program will randomly choose a new number each time you connect. You can always try again, but you should start your binary search over from the beginning - try around 500. Can you think of why?
## Solution
Connect to the target program using nc (netcat). The program hides the flag by asking you to guess a number in the range 1–1000 and uses binary search logic to narrow the answer. Binary search is an efficient algorithm that halves the search space each guess instead of trying every number one-by-one.
How to solve it:

1. The program asks you to guess a number between 1 and 1000.  
2. Always guess the middle of the current range. Start with 500.  
3. The program will respond with one of:  
    - Higher — your guess is too low → update the lower bound to guess + 1.
    - Lower — your guess is too high → update the upper bound to guess - 1.
    - Correct (or prints the flag) — you found the value.
4. Repeat the process (guess the midpoint of the updated range) until you receive the flag.

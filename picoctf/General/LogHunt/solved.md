# TITLE : Log Hunt
## Author : Yahaya Meddy
## Description
Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag?
Download the [logs](https://challenge-files.picoctf.net/c_amiable_citadel/49cec6157142f24a599f4164d5b63322c2494f801390d6f22eb91b3aa592bc66/server.log) and figure out the full flag from the fragments.
## Hints
- You can use grep to filter only matching lines from the log.
- Some lines are duplicates; ignore extra occurrences.
## Solution
In this challenge, we were given a server log file. I used the `cat` command to view the contents of the file and discovered a flag inside. The flag was divided into four separate parts, and combining these parts revealed the complete flag.

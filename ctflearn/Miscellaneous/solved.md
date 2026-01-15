# TITLE : Rock Paper Scissors
## Author : intelagent
## Description
Do you think you're lucky enough to win 10 games of Rock Paper Scissors in a row? Connect to the server and find out. `nc 138.197.193.132 5001`
## Solution
In this challenge, we were required to connect to the service using netcat. The service hosted a Rock–Paper–Scissors game.

Initially, I connected to the server multiple times to observe its behavior. After several attempts, I realized that each round followed a deterministic pattern—the server consistently responded with the same sequence of moves.

To confirm this, I played through 10 rounds and recorded the server’s responses. From this observation, I derived the following winning pattern:
```
PRPSPPSPRP
```
I then reconnected to the service and replayed the game using this exact pattern. As expected, this allowed me to win every round, and the server returned the flag.

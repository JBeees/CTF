# TITLE : Shop
## Author : thelshell
## Description
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://mercury.picoctf.net/static/73724c199e55e6c056bb00e7bbfdfb38/source). The shop is open for business at nc mercury.picoctf.net 10337.
## Hints
- Always check edge cases when programming
## Solution
In this challenge, we were given a C program about shopping items. We could buy an item and specify the quantity we wanted. Among the options, there was item number 2, which represented the flag and cost 100. However, at the start we only had 40 money.

I discovered that the program didn’t properly handle negative values for the quantity. For example, if an item cost 10 and I entered `-1` as the quantity, my money actually increased instead of decreasing. Using this bug, I repeatedly exploited the negative quantity input to increase my money until it reached 100.

Once I had enough money, I selected the flag option and successfully obtained the flag.

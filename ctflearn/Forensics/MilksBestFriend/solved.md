# TITLE : Milk's Best Friend
## Author : bobbyjives
## Description
There's nothing I love more than oreos, lions, and winning. https://mega.nz/#!DC5F2KgR!P8UotyST_6n2iW5BS1yYnum8KnU0-2Amw2nq3UoMq0Y Have Fun :)
## Solution
In this challenge, we were given a JPG file. I analyzed the file using `binwalk`, which revealed an embedded RAR archive. After extracting it, a directory was created containing another JPG file named `b`. I then ran the `strings` command on this file and was able to locate the flag.

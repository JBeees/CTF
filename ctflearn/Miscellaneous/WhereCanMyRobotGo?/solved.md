# TITLE : Where Can My Robot Go?
## Author : intelagent
## Description
Where do robots find what pages are on a website?
Hint:
What does disallow tell a robot?
## Solution
In this challenge, the topic was robots on a website, so I checked the site’s robots.txt file by accessing:
```
https://ctflearn.com/robots.txt
```
Inside the file, I found the following directive:
```
User-agent: *
Disallow: /70r3hnanldfspufdsoifnlds.html
```
The Disallow directive tells search engine robots not to crawl the specified path. However, it also reveals the existence of that page.
I then manually accessed the disallowed path:
```
https://ctflearn.com/70r3hnanldfspufdsoifnlds.html
```
On that page, I found the flag, which completed the challenge.

# TITLE : Combo Safe-box
## Author : thekidofarcrania
## Description
My friend likes to keep secret stuff inside a safe-box.

I have kept bugging him for the combination to the safe. He finally gave this link: https://mega.nz/#!KP5XwZTA!KPEHBt-w-5x-9_7mevBAQo5AGcs82gQSQKscae34jnA to me. When I opened it I got this puzzling combo box. He told me "Follow the links down the rabbit-hole! There's only one correct path!"<br />

Can you figure out the combination safe lock?
## Solution
In this challenge, we were given a PPTX file that contained a puzzle about finding a numeric combination. The correct combination is obtained by clicking numbers along the correct navigation path until reaching the success page.

First, I unzipped the PPTX file to inspect its internal structure. I then navigated to the following directory, where slide redirection logic is stored:
```
ppt/slides/_rels/
```
To trace the correct navigation path, I searched for references to the final slide, which I identified as slide14.xml. I used the following command:
```
grep -R slide14 .
```
This allowed me to find all slides that redirect to the final page. From there, I worked backwards, identifying each slide that linked to the previous one.

For each slide in the path, I:
- Opened the corresponding slide
- Clicked the number shown on that slide
- Followed the correct redirection link
I repeated this process until I reached the starting slide.
By following the only valid path to the success page, I obtained the following numeric combination:
```
751623
```
Finally, wrapping the combination with `CTFlearn{}` gives the flag.

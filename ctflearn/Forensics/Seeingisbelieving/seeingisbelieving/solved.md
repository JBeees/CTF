# TITLE : Seeing is believing
## Author : sengokumedaru
## Description
My colleague's an astronaut who's currently on a mission orbiting in space. Just a few hours ago, unfortunately, his communication device caught fire so he's unable to report back to base. I did, however, receive a strange file that I can't seem to open. I think it may shed some light on his situation. Can you help me save poor boy Johnny? File: https://mega.nz/#!LTRUTaZb!9Nh0NwDONJQiOThif3G62evP8H_W9eIJSu0PdBQWKyg
## Solution
In this challenge, we are given a ZIP file. After extracting it, we find an .ogg file, which is an audio file.

To analyze the audio for hidden data, we play it using ffplay with a spectrogram visualization:
```
ffplay -f lavfi -i "amovie=help.me,showspectrumpic=s=1024x1024"
```
This command generates a spectrogram image of the audio. Upon visual inspection, a QR code appears in the spectrogram.

By scanning the QR code, we obtain the flag.

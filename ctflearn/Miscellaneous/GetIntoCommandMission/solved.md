# TITLE : Get Into Command Mission
## Author : pian
## Description
Back into the mission. Since we struck one fugitive successfully, we found an ID Card named ALDI and a flashdisk which contain a program (https://mega.nz/#!KXYEQaIJ!ima4afmEP59Z1kKTm0H-3vO2x2UPdvNYKhUDdb3Vbr0). Unfortunately, it was locked. Note: You do NOT need a specific operating system to solve this question.
## Solution
In this challenge, we were given a .exe file to analyze. I began with static analysis using the strings utility to inspect readable data embedded in the binary.

During this process, I discovered a Base64-encoded image, identifiable by the following prefix:
```
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAfQAAAH0CAIAAABEtEjdAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUIIFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKOg6OIisr74Xuja9a89+bN/rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz...
```
This indicated that the executable contained an embedded PNG image encoded in Base64.

I extracted the Base64 string and saved it to a file. After decoding it using the base64 utility, the output produced a valid PNG image. Opening the image revealed the flag.

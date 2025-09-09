# TITLE : Blast from the past
## Author : syreal
## Description
The judge for these pictures is a real fan of antiques. Can you age this photo to the specifications?
Set the timestamps on this picture to 1970:01:01 00:00:00.001+00:00 with as much precision as possible for each timestamp. In this example, +00:00 is a timezone adjustment. Any timezone is acceptable as long as the time is equivalent. As an example, this timestamp is acceptable as well: 1969:12:31 19:00:00.001-05:00. For timestamps without a timezone adjustment, put them in GMT time (+00:00). The checker program provides the timestamp needed for each.
Use this picture.
Submit your modified picture here:
nc -w 2 mimas.picoctf.net 64310 < original_modified.jpg
Check your modified picture here:
nc mimas.picoctf.net 55020
## Hints
- Exiftool is really good at reading metadata, but you might want to use something else to modify it.
## Solution
In this challenge, we are given an image, and we are asked to modify certain metadata values before submitting it to the server. The tags we need to change are:

```yaml
Looking at IFD0: ModifyDate
Looking for '1970:01:01 00:00:00'
Found: 2023:11:20 15:46:23

Looking at ExifIFD: DateTimeOriginal
Looking for '1970:01:01 00:00:00'
Found: 2023:11:20 15:46:23

Looking at ExifIFD: CreateDate
Looking for '1970:01:01 00:00:00'
Found: 2023:11:20 15:46:23

Looking at Composite: SubSecCreateDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.70

Looking at Composite: SubSecDateTimeOriginal
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001

Looking at Composite: SubSecModifyDate
Looking for '1970:01:01 00:00:00.001'
Found: 1970:01:01 00:00:00.001

Looking at Samsung: TimeStamp
Looking for '1970:01:01 00:00:00.001+00:00'
Found: 2023:11:20 20:46:21.420+00:00
```
**Step 1: Modifying standard Exif tags**

For all tags except the 7th tag (Samsung: TimeStamp), you can use ExifTool to change the values:
```bash
exiftool -<TagName>="<value>" <image_name>
```
To verify the changes:
```bash
exiftool -<TagName> <image_name>
```
**Step 2: Modifying the Samsung TimeStamp**

The 7th tag (Samsung: TimeStamp) cannot be modified using ExifTool. To change it:
1. Use strings on the image to locate the timestamp value:
```
Image_UTC_Data1700513181420
```
2. Convert the numeric part (1700513181420) from milliseconds since epoch using an epoch converter. This gives:
```
GMT: Monday, November 20, 2023 8:46:21.420 PM
```
This corresponds to the current value of the Samsung timestamp.  

3. Using a hex editor, locate this value (Image_UTC_Data1700513181420) and modify it to the required value:
```
Image_UTC_Data000000000001
``` 
Tip: Using Ctrl + S in the hex editor helps you quickly find this part in the file.
4. Save the changes and submit the image. The server should now accept it, and you will be able to retrieve the flag.

# TITLE : Event-Viewing
## Author : Venax
## Description
One of the employees at your company has their computer infected by malware! Turns out every time they try to switch on the computer, it shuts down right after they log in. The story given by the employee is as follows:
1. They installed software using an installer they downloaded online
2. They ran the installed software but it seemed to do nothing
3. Now every time they bootup and login to their computer, a black command prompt screen quickly opens and closes and their computer shuts down instantly.
See if you can find evidence for the each of these events and retrieve the flag (split into 3 pieces) from the correct logs!
Download the Windows Log file [here](https://challenge-files.picoctf.net/c_verbal_sleep/123d9b79cadb6b44ab6ae912f25bf9cc18498e8addee851e7d349416c7ffc1e1/Windows_Logs.evtx)
## Hints 
- Try to filter the logs with the right event ID
- What could the software have done when it was ran that causes the shutdowns every time the system starts up?
## Solution
In this challenge we were given a .evtx file (Windows Event Log). To make the log readable, I converted it to XML using the following script:
```python
from Evtx import Evtx

input_file = "Windows_Logs.evtx"
output_file = "output.xml"

with Evtx.Evtx(input_file) as log:
    with open(output_file, "w", encoding="utf-8") as f:
        for record in log.records():
            f.write(record.xml())
            f.write("\n")
```
After converting, I searched for evidence related to shutdown because the problem description mentions the system shutting down after login. I found an event with **Event ID 1074** — this event is logged when an application or user initiates a shutdown or restart. Inside that event I found a Base64-encoded string in the shutdown reason; decoding it reveals the third piece of the flag.

Next, I searched for persistence indicators and found an entry referring to custom_shutdown.exe in the registry. This appears in an **Event ID 4657** record. Event 4657 logs when a registry value is created or modified. The malware created a Run-key entry named Immediate Shutdown (MXNfYV9wcjN0dHlfdXMzZnVsXw==) pointing to `C:\Program Files (x86)\Totally_Legit_Software\custom_shutdown.exe`. Decoding that Base64 string gives the second piece of the flag.

Finally, I looked for installation evidence. The installer activity was recorded by Windows Installer — the relevant MSI install event is **Event ID** 1033 (MsiInstaller). I found a record showing `Totally_Legit_Software` was installed successfully; that entry contains a Base64-encoded fragment that decodes to the first piece of the flag.

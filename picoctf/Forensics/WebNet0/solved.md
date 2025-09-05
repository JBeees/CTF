# TITLE : WebNet0
## Author : WebNet0
## Description
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/capture.pcap) and [key](https://jupiter.challenges.picoctf.org/static/0c84d3636dd088d9fe4efd5d0d869a06/picopico.key). Recover the flag.
## Hints 
- Try using a tool like Wireshark.
- How can you decrypt the TLS stream?
## Solution
In this challenge, we were given a packet capture file and a private key file. I opened the capture in **Wireshark** and noticed that it contained **TLS traffic**, which is a cryptographic protocol used to provide secure communication over a computer network.

Within these TLS packets, the data was encrypted. Since we were also provided with the private key, I realized that it could be used to decrypt the TLS traffic.
    
In Wireshark, I went to:
```
Edit → Preferences → Protocols → TLS → Edit RSA Keys List
```
Then I filled in the fields as follows:
- IP address: Server IP that uses TLS
- Port: 443
- Protocol: http
- Key File: Path to the provided private key
- Password: Leave empty

After clicking **OK**, I applied a filter for `tls`. The previously encrypted packets were now decrypted.

Looking at **packet number 32**, under the **HTTP details**, I found the `Pico-Flag` field which contained the flag.

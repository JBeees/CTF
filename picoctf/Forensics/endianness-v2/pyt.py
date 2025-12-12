data = open("challengefile", "rb").read()
out = bytearray()

for i in range(0, len(data), 4):
    out.append(data[i+3])
    out.append(data[i+2])
    out.append(data[i+1])
    out.append(data[i])     
open("fixed.jpg", "wb").write(out)


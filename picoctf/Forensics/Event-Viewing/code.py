from Evtx import Evtx

input_file = "Windows_Logs.evtx"
output_file = "output.xml"

with Evtx.Evtx(input_file) as log:
    with open(output_file, "w", encoding="utf-8") as f:
        for record in log.records():
            f.write(record.xml())
            f.write("\n")


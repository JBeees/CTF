
with open("input.txt") as f:
    content = f.read().strip()

##print(content)
res = eval(content)
for line in res:
    if isinstance(line, list) and line:   # make sure it's a non-empty list
        first = line[0]
        last = line[-1]
        print("first:", first, " last:", last)

import string

def map_text(text):
    result = ""
    i = 0
    for ch in text:
        if (i % 2 == 0):
            result += chr((ord(ch) - 5) % 256)
        else:
            result += chr((ord(ch) + 2) % 256)
        i+=1
    return result

text = "w1{1wq8/7376j.:"

res = map_text(text)

print("Original  :", text)
print("Result", res)


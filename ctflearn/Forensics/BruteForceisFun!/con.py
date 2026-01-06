import hashlib
hash_check = "e82a4b4a0386d5232d52337f36d2ab73"
for i in range(100000):
    s = str(i).zfill(5)
    testing = "ctflag"+str(i)
    if hashlib.md5(testing.encode()).hexdigest() == hash_check:
        print("Found:", i)
        break
    print(s)

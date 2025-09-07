import hashlib
username_trial = b"FRASER"
c=""
c+=hashlib.sha256(username_trial).hexdigest()[4]
c+=hashlib.sha256(username_trial).hexdigest()[5]
c+=hashlib.sha256(username_trial).hexdigest()[3]
c+=hashlib.sha256(username_trial).hexdigest()[6]
c+=hashlib.sha256(username_trial).hexdigest()[2]
c+=hashlib.sha256(username_trial).hexdigest()[7]
c+=hashlib.sha256(username_trial).hexdigest()[1]
c+=hashlib.sha256(username_trial).hexdigest()[8]
print(c)

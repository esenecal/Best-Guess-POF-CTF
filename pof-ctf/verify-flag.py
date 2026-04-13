#!/usr/bin/env python3
import sys
import hashlib

# verify the ctf (passed in via command line) is correct.

m = hashlib.sha256()        # prepare encoding in sha256
m.update(sys.argv[1].encode('utf-8'))   # encode second argument in command line (after .py), hash.

if(m.hexdigest() == "e9d8d16c3e2ff6d98558175a8301febd2a34f20d44451b51ef0b7db15ffa18fa"):    # ensure the hashed flag is correct by ensuring it matches the expected hash.
    print("Correct!")
else:
    print("Incorrect")
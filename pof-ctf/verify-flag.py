#!/usr/bin/env python3
import sys
import hashlib

# verify the ctf (passed in via command line) is correct.

m = hashlib.sha256()        # prepare encoding in sha256
m.update(sys.argv[1].encode('utf-8'))   # encode second argument in command line (after .py), hash.

if(m.hexdigest() == "aa2c1e333f167d997974d3e33f76266057dc2f9c1bae971f263abc28d1937842"):    # ensure the hashed flag is correct by ensuring it matches the expected hash.
    print("Correct!")
else:
    print("Incorrect")
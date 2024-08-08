import pyimager as pi
import time, os
path = "./"+input("Namen eingeben: ")+".lkim"
tgt = "./"+input("Zieldatei angeben: ")+".lkim"
print(os.stat(path).st_size)
pi.compressor(path, tgt, True)
pi.display(tgt)
print(os.stat(tgt).st_size)
time.sleep(3)

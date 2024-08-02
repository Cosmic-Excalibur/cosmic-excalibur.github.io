from pwn import *
context(log_level = 'debug')

r = remote('be.ax', 32422)

r.recvuntil(b'solution: ')
r.sendline(input('PoW: '))

r.sendlineafter(b'Select a sensor index to remove from each bit: ', b'5 5 5 5 5 5 5 5')
r.recvuntil(b"Here's your flag: b'")
flag = bytes.fromhex(r.recvuntil(b"'", drop = 1).decode())

key = []

while 1:
    r.recvuntil(b'Sensor measurements: ')
    measurements = r.recvline().strip().decode()

    r.sendlineafter(b'or r for res.\n', (b'cx 6 r;cx 1 r;cx 2 r\n'*8)[:-1])

    r.recvuntil(b'Your byte: ')
    byte = r.recvline().strip().decode()

    patterns = ['110', '010', '100']
    measures = [measurements[6*i:6*i+3] for i in range(8)]
    real_byte = ''
    for i, m in enumerate(measures):
        if m in patterns:
            real_byte += '0' if byte[i] == '1' else '1'
        else:
            real_byte += byte[i]

    #success(real_byte)
    key.append(int(real_byte, 2))
    success(str(bytes(key)))
    success(str(flag))



r.interactive()
r.close()
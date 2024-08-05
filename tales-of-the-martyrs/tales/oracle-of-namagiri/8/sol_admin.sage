# https://meowmeowxw.gitlab.io/ctf/utctf-2020-crypto/

from Crypto.Util.number import long_to_bytes as lb
from Crypto.Util.number import bytes_to_long as bl
from binascii import unhexlify, hexlify
from sage.all import *
import struct

def bytes_to_polynomial(block, a):
    poly = 0
    # pad to 128
    bin_block = bin(bl(block))[2 :].zfill(128)
    # reverse it to count correctly, wrong don't reverse it lol
    # bin_block = bin_block[::-1]
    for i in range(len(bin_block)):
        poly += a^i * int(bin_block[i])
    return poly

def polynomial_to_bytes(poly):
    return lb(int(bin(poly.integer_representation())[2:].zfill(128)[::-1], 2))

def convert_to_blocks(ciphertext):
    return [ciphertext[i:i + 16] for i in range(0 , len(ciphertext), 16)]

def xor(s1, s2):
    if(len(s1) == 1 and len(s1) == 1):
        return bytes([ord(s1) ^^ ord(s2)])
    else:
        return bytes(x ^^ y for x, y in zip(s1, s2))

F, a = GF(2^128, name="a", modulus=x^128 + x^7 + x^2 + x + 1).objgen()
R, x = PolynomialRing(F, name="x").objgen()

# Set correct values
C1 = convert_to_blocks(bytes.fromhex("ca6a3e623d125bdcddfe5c6e0ecba0911162c4f4469a62c32f1598ce9b161f92"))
T1 = bytes.fromhex("79be7f8880af8d18b8abac496fb690d2")
C2 = convert_to_blocks(bytes.fromhex("ca6a3e623d125bdcddfe5c6e0ecba0911162c4f5469a62c32f1598ce9b161f92"))
T2 = bytes.fromhex("abb63fd177e59f360ef2b3786e7fe4a9")
C3 = convert_to_blocks(bytes.fromhex("c5612754327d3dbeb8aa221660b2c5fb"))

L = struct.pack(">QQ", 0 * 8, len(C1) * 8*16)
C1_p = [bytes_to_polynomial(C1[i], a) for i in range(len(C1))]
C2_p = [bytes_to_polynomial(C2[i], a) for i in range(len(C2))]
C3_p = [bytes_to_polynomial(C3[i], a) for i in range(len(C3))]
T1_p = bytes_to_polynomial(T1, a)
T2_p = bytes_to_polynomial(T2, a)
L_p = bytes_to_polynomial(L, a)
L3 = struct.pack(">QQ", 0 * 8, len(C3) * 8*16)
L3_p = bytes_to_polynomial(L3, a)
# Here G_1 is already modified to include the tag
G_1 = (C1_p[0] * x^3) + (C1_p[1] * x^2) + (L_p * x) + T1_p
G_2 = (C2_p[0] * x^3) + (C2_p[1] * x^2) + (L_p * x) + T2_p
G_3 = (C3_p[0] * x^2) + (L3_p * x)
P = G_1 + G_2
auth_keys = [r for r, _ in P.roots()]
for H, _ in P.roots():
    EJ = G_1(H)
    T3 = G_3(H) + EJ
    print("H: " + str(H) + "\nT3: " + str(polynomial_to_bytes(T3).hex()))
from Crypto.Util.number import *
N = 0xFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123
ciphertext = b"a\x16iu\x86\xb1/\xb66\xe3\xc3\xb2q\x80\xfc\xa6;9\xafF\xe9\x83\xf2\xa2\xde\xf2\x1f\xbeP\xd4T\xaeu\xee\xed\xac\xdd\x19\x8b\x91<>\xda\x05$\x0e\x0fO#}u_W\xfb\x16SB\x87V\x83\x7f~\x0evf'\x94\xbf\x9d\xee\xae&b\xcbw\x06\xf4\x9c\xa3\x00\xef/\xf2\t\xd5\xf9:\xd67\x0f\xa0\xfe\x82j)\xd8\xb8\x04[;\x19&\xe2\xa7\x95\xd0\x86\x1b?\xc20\xd0E\x05S\xadwj\x96#\xb1Bp\xa6\x83\xe5T5"
k = (bytes_to_long(ciphertext[:32]))*pow(bytes_to_long(b"CryptoCup message:"[:16]),-1,N)%N
print(long_to_bytes(bytes_to_long(ciphertext[32:32+32])*pow(int(k)+1,-1,N)%N))
print(long_to_bytes(bytes_to_long(ciphertext[64:64+32])*pow(int(k)+2,-1,N)%N))
print(long_to_bytes(bytes_to_long(ciphertext[96:96+32])*pow(int(k)+3,-1,N)%N))

xs = [0x90fc5cf2, 0xe2f47488, 0xa257fd51, 0xe0ae615b]

MULTIPLIER = 6364136223846793005
ADDEND = 1
MASK = 0xffffffffffffffff
ITERATIONS = 1000
a = pow(MULTIPLIER, ITERATIONS, MASK+1)
b = sum(ADDEND*pow(MULTIPLIER, i, MASK+1) for i in range(ITERATIONS)) % (MASK+1)
n = len(xs)

A = matrix(ZZ, n*2, n*2)

for i in range(n-1):
    A[i, i] = a
    A[i+1, i] = -1
    A[n, i] = a*(xs[i] << 32) + b - (xs[i+1] << 32)
    A[n+i+1, i] = MASK+1
for i in range(n+1):
    A[i, n+i-1] = 1
A[n, n+n-1] = 10**100
for i in range(n-1):
    A[:, i] *= 10**100
for i in range(n):
    A[:, i+n-1] *= 10**0
A_ = A.LLL()
v = A_[-1]

print(v[3:7])

seed = v[6]//10**0 + (xs[-1] << 32)


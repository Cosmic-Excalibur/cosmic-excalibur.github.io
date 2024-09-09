def kannan_cvp(mat, target, reduction=(lambda x: x.LLL()), weight=None):
    """
    Solve closest vector problem using Kannan's algorithm

    :param mat: a matrix
    :param target: a vector
    :returns: a solution as a vector
    """
    if weight is None:
        weight = max(target)
    L = block_matrix([[mat, 0], [-matrix(target), weight]])
    for row in reduction(L):
        if row[-1] < 0:
            row = -row
        if row[-1] == weight:
            return row[:-1] + target

xs = [0x90fc5cf2, 0xe2f47488, 0xa257fd51, 0xe0ae615b]

MULTIPLIER = 6364136223846793005
ADDEND = 1
MASK = 0xffffffffffffffff
ITERATIONS = 1000
a = pow(MULTIPLIER, ITERATIONS, MASK+1)
b = sum(ADDEND*pow(MULTIPLIER, i, MASK+1) for i in range(ITERATIONS)) % (MASK+1)
n = len(xs)

B = matrix(ZZ, n, n)

for i in range(n):
    B[i, i] = MASK + 1
    B[0, i] = a**i

c = 2**32//2

bs = [0]
for i in range(n-1):
    bs.append(b + a*bs[-1])
t = vector(c + (xs[i] << 32) - bs[i] for i in range(n))

v = kannan_cvp(B, t)
v = [v[i] - (xs[i] << 32) + bs[i] for i in range(n)]

print(v)

seed = v[-1] + (xs[-1] << 32)

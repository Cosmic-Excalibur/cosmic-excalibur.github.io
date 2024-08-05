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

def babai_cvp(mat, target, reduction=(lambda x: x.LLL())):
    M = reduction(matrix(ZZ, mat))
    G = M.gram_schmidt()[0]
    diff = target
    for i in reversed(range(G.nrows())):
        diff -= M[i] * ((diff * G[i]) / (G[i] * G[i])).round()
    return target - diff

set_random_seed(1337)
Fp = GF(6143872265871328074704442651454311068421530353607832481181)
a, b = Fp.random_element(), Fp.random_element()
p = 18315300953692143461
z3 = Fp.gen()

m0, m1, m2, _ = Fp.modulus()
a0, a1, a2 = a
b0, b1, b2 = b

c = [50, 32, 83, 12, 49, 34, 81, 101, 46, 108, 106, 57, 105, 115, 102, 51, 67, 34, 124, 15, 125, 117, 51, 124, 38, 10, 30, 76, 125, 27, 89, 14, 50, 93, 88, 56]
n = len(c)
A = matrix(ZZ, n + 1, n - 3)
shift = 57
for i in range(n//3 - 1):
    ci0 = c[i*3 + 0] << shift
    ci1 = c[i*3 + 1] << shift
    ci2 = c[i*3 + 2] << shift
    ci0_ = c[i*3 + 3] << shift
    ci1_ = c[i*3 + 4] << shift
    ci2_ = c[i*3 + 5] << shift
    row = i*3
    col = i*3 + 0
    A[row + 0, col] = a0
    A[row + 1, col] = -a2*m0
    A[row + 2, col] = -a1*m0 + a2*m0*m2
    A[row + 3, col] = -1
    A[-1, col] = a0*ci0 + b0 - (a2*ci1 + a1*ci2)*m0 + a2*ci2*m0*m2 - ci0_
    col = i*3 + 1
    A[row + 0, col] = a1
    A[row + 1, col] = a0 - a2*m1
    A[row + 2, col] = -a1*m1 + a2*(m1*m2-m0)
    A[row + 4, col] = -1
    A[-1, col] = a0*ci1 + a1*ci0 + b1 - (a2*ci1 + a1*ci2)*m1 + a2*ci2*(m1*m2-m0) - ci1_
    col = i*3 + 2
    A[row + 0, col] = a2
    A[row + 1, col] = a1 - a2*m2
    A[row + 2, col] = a0 - a1*m2 + a2*(m2**2-m1)
    A[row + 5, col] = -1
    A[-1, col] = (a2*ci0 + a1*ci1 + a0*ci2) + b2 - (a2*ci1 + a1*ci2)*m2 + a2*ci2*(m2**2-m1) - ci2_

A1 = block_matrix([[A, 1],[p, 0]])

beta = 2**100
for i in range(A.dimensions()[0] - 1):
    if i % 6 >= 3:
        A1[:, i + A.dimensions()[1]] *= 1
A1[A.dimensions()[0] - 1, -1] *= beta
A1[:, :n-3] *= beta

A_ = A1.LLL()

f = lambda x: round(2**(x-1)+(2**x-2**(x-1))/2)
center = [0]*A.dimensions()[1] + [f(56) for i in range(A.dimensions()[0]-1)] + [beta]

# The same
v1 = kannan_cvp(A1, vector(center))
print(v1)
v2 = babai_cvp(A1, vector(center))
print(v2)
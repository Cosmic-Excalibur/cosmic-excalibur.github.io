INFO = {
    'title': r'2024 WMCTF Write-ups',
    'tags': ['CTF', 'WMCTF', 'Cryptography', 'ClassicalCiphers', 'LatticeBasedCryptography', 'GraphTheory', 'LinearAlgebra'],
    'time': '2024-09-10 15:48'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
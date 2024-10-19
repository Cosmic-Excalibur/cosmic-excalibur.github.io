INFO = {
    'title': r'2024 熵密杯 Write-ups',
    'tags': ['CTF', '熵密杯', 'Cryptography', 'LatticeBasedCryptography', 'LinearCongruentialGenerator'],
    'time': '2024-09-09 16:34'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
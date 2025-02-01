INFO = {
    'title': r'ECC Megamix',
    'tags': ['AlgebraicNumberTheory', 'EllipticCurveCryptography'],
    'time': '2024-02-01 20:50'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
INFO = {
    'title': r'Non-degenerate Loops in CSIDH',
    'tags': ['AlgebraicNumberTheory', 'EllipticCurveCryptography', 'HomologyTheory', 'IsogenyBasedCryptography'],
    'time': '2025-02-28 15:34'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
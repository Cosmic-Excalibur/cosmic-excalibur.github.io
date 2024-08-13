INFO = {
    'title': r'Notes on the Proof of ANT Thm. 3.7',
    'tags': ['AlgebraicNumberTheory'],
    'time': '2024-08-12 19:37'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
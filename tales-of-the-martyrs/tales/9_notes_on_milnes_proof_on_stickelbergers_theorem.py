INFO = {
    'title': r"Notes on Milne's Proof on Stickelberger's Theorem",
    'tags': ['AlgebraicNumberTheory'],
    'time': '2024-08-06 00:16'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
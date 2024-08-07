INFO = {
    'title': r'ANT Chapter 2 Exercises',
    'tags': ["AlgebraicNumberTheory"],
    'time': '2024-08-07 18:49'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
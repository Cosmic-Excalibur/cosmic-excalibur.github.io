INFO = {
    'title': 'Alkane counting problems',
    'tags': ['Mathematics', 'GroupTheory', 'Combinatorics', 'OI'],
    'time': '2024-07-06 23:10'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
INFO = {
    'title': r'2018 QCTF babyheap',
    'tags': ['Pwn', 'BinaryExploitation', 'HeapExploitation', 'OffByNull'],
    'time': '2024-07-13 14:58'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
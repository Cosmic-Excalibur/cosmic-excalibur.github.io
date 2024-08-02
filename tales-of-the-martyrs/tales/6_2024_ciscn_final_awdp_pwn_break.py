INFO = {
    'title': r'2024 CISCN Final AWDP Pwn Break',
    'tags': ['Pwn', 'BinaryExploitation', 'CISCN'],
    'time': '2024-08-02 21:42'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
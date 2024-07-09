INFO = {
    'title': r'Continuity at \(\mathbb{Q}\) and \(\mathbb{R}\backslash\mathbb{Q}\)',
    'tags': ['Mathematics', 'GeneralTopology', 'FunctionalAnalysis', 'RealAnalysis'],
    'time': '2024-07-09 16:35'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
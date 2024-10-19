INFO = {
    'title': r'2024 MoeCTF Write-ups/Archive',
    'tags': ['CTF', 'MoeCTF'],
    'time': '2024-10-19 20:17'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read(),
        __HTML_TITLE__: '2024 MoeCTF <span style="color:gray"><s>Write-ups</s></span>Archive'
    }
}
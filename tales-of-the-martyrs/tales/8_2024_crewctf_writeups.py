INFO = {
    'title': r'2024 CrewCTF Write-ups',
    'tags': ['CrewCTF', 'Cryptography', 'ReverseEngineering', 'LatticeBasedCryptography', 'LinearCongruentialGenerator', 'BlockCipher', 'AES-GCM', 'HTML-TheProgrammingLanguage'],
    'time': '2024-08-05 14:23'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
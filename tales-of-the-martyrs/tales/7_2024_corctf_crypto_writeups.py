INFO = {
    'title': r'2024 corCTF Crypto Write-ups',
    'tags': ['corCTF', 'Cryptography', 'LatticeBasedCryptography', 'QuantumCircuit'],
    'time': '2024-08-02 22:09'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
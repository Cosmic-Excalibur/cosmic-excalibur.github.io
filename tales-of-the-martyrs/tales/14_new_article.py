INFO = {
    'title': r'2024 SpiritCTF Warmup Write-ups by Astrageldon',
    'tags': ['SpiritCTF'],
    'time': '2024-10-03 10:49'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: open(".".join(path.split(".")[:-1]) + ".data", 'r', encoding = 'utf-8').read()
    }
}
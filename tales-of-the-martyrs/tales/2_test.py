INFO = {
    'title': 'TEST2',
    'tags': ['test', 'nothing', 'Astrageldon!'],
    'time': '2024-07-06 14:04'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: r"""
        
        <div class="main">
            <p>This is a test by <span class="astrageldon">Astrageldon</span>!</p>
        </div>
        
        """
    }
}
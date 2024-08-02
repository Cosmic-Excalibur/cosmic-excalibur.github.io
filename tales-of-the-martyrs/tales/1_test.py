INFO = {
    'title': 'TEST!',
    'tags': ['test', 'nothing', 'doro'],
    'time': '2024-07-06 13:30'
}

def info():
    return Attrs(INFO)
    
data = lambda: {
    "*.html": {
        __CONTENT__: r"""
        
        <div class="main">
            <p>This is a test by <span class="astrageldon">Astrageldon</span>!</p>
            <p>And below is the Maxwell equations in their differential form:</p><br>
            <p>
            \[
            \newcommand{\bs}{\boldsymbol}
            \left\{
            \begin{aligned}
            \bs{\nabla}\cdot\bs{E}&=\frac{\rho}{\varepsilon_0}\\
            \bs{\nabla}\times\bs{E}&=-\frac{\partial\bs B}{\partial t}\\
            \bs{\nabla}\cdot\bs{B}&=0\\
            \bs{\nabla}\times\bs{B}&=\mu_0\bs{j}+\mu_0\varepsilon_0\frac{\partial\bs E}{\partial t}
            \end{aligned}
            \right.
            \]
            </p><br>
            <p>And below is a ...</p>
            <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
            <p>Doro!!!</p><br>
            <div class="center">
            <img src="__ASSETS__/1.gif" alt="doro!"></img>
            <br><br>
            <img width=600 src="__ASSETS__/2.gif" alt="doro!"></img>
            </div>
        </div>
        
        """
    }
}
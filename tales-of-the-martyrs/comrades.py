entries = {
    'Astrageldon': ['https://cosmic-excalibur.github.io'],
    'Astrageldon <comment>(Github)</comment>': ['https://github.com/Cosmic-Excalibur'],
    'Tplus': ['https://www.tpluszz.top'],
    '<s>App1e_Tree</s> <comment>(Outdated)</comment>': ['https://www.cnblogs.com/App1eTree'],
    'App1e_Tree': ['https://yinwww.wang'],
    'LiBr': ['https://nvme0n1p.dev'],
    'LiBr <comment>(Github)</comment>': ['https://github.com/lbr77'],
    'CrackTC': ['https://sora.zip'],
    'CrackTC <comment>(Github)</comment>': ['https://github.com/CrackTC'],
    'emmm <comment>(Github)</comment>': ['https://github.com/H4ckF0rFun'],
    'Spirit Team': ['https://jluctf.top', 'https://spirit.college'],
    'PJSK Stickers': ['https://trpde.github.io']
}

def parse_entry(entries):
    return [
        [entry[0], "<br>".join("""{0}<a underlined href="{1}">{1}</a>""".format("""<span style="color:gray">Link: </span>""" if i == 0 else """<span style="color:gray">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>""", link) for i, link in enumerate(entry[1]))] for entry in list(entries.items())
    ]

data = lambda: {
    "*.html": {
        __TITLE__: r"""Friends""",
        __HTML_TITLE__: r"""~ Friends ~""",
        __CONTENT__: "<br>\n".join(
                r"""<hr>
                <div style="margin-left:2em">
                    <h2>{0}</h2>
                    {1}
                </div>
                """.format(*entry) for entry in parse_entry(entries)
            ) + "\n<br><br><hr><br><br>"
    }
}
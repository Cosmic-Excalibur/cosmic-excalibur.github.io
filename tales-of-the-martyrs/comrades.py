entries = {
    'Astrageldon': 'https://cosmic-excalibur.github.io',
    'Tplus': 'https://www.tpluszz.top',
    'App1e_Tree': 'https://www.cnblogs.com/App1eTree',
    'LiBr': 'https://nvme0n1p.dev'
}

def parse_entry(entries):
    return [
        entry for entry in list(entries.items())
    ]

data = lambda: {
    "*.html": {
        __TITLE__: r"""Friends""",
        __HTML_TITLE__: r"""~ Friends ~""",
        __CONTENT__: "<br>\n".join(
                r"""<hr>
                <div style="margin-left:2em">
                    <h2>{0}</h2>
                    <span style="color:gray">Link🔗: </span><a underlined href="{1}">{1}</a>
                </div>
                """.format(*entry) for entry in parse_entry(entries)
            ) + "\n<br><br><hr><br><br>"
    }
}
import os

tales = os.path.join(workdir, "tales-of-the-martyrs", "tales")
tales_web = '/tales-of-the-martyrs/tales/'
interval = 10

def parse_info(filename, info):
    title = info.title
    tags = info.tags
    time = info.time
    return (tales_web + '.'.join(filename.split('.')[:-1]) + '.html', title, '</b></span><span color="gray">, </span><span style="color:blue"><b>'.join('#%s' % tag for tag in tags), time)

entries = sorted(os.listdir(tales))
entries = [entry for entry in entries if entry.endswith('.py')]

data = lambda: dict([
    (f"*_{i+1}.html", {
        __TITLE__: r"""Categories""",
        __HTML_TITLE__: r"""Categories""",
        __CONTENT__: "<br>\n".join(
                r"""<hr>
                <div style="margin-left:2em">
                    <h2><a href="%s">%s</a></h2>
                    <span style="color:gray">Tags: <span style="color:blue"><b>%s</b></span>
                    <br><br>
                    </span>
                    <div class="time"></div><span><span style="color:gray">Time: </span><b>%s</b></span>
                </div>
                """ % parse_info(entries[j], import2(os.path.join(tales, entries[j]), encoding = 'utf-8').info()) for j in range(i, min(len(entries), i+interval))
            ) + "\n<br><br><hr>"
        }) for i in range(0, len(entries), interval)
])
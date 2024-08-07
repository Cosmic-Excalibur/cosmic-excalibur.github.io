import os

tales = os.path.join(workdir, "tales-of-the-martyrs", "tales")
tales_web = '/tales-of-the-martyrs/tales/'
page = '/tales-of-the-martyrs/domains-of-the-hallow_'
interval = 10

def parse_info(filename, info):
    title = info.title
    tags = info.tags
    time = info.time
    return (tales_web + '.'.join(filename.split('.')[:-1]) + '.html', title, '</b></span><span color="gray">, </span><span style="color:blue"><b>'.join('#%s' % tag for tag in tags), time)

entries = sorted([f for f in os.listdir(tales) if f.endswith('.py')], key = lambda x: -int(x.split('_')[0]))
entries = [entry for entry in entries if entry.endswith('.py')]
pages = len(entries) // interval + 1 if len(entries) % interval else len(entries) // interval

tail = r"""
<br><br><hr>
<br><br>
<div class="center">
    <span>Page: <input class="pagination" type="number" value="{0}" max="{1}" min="1" onchange="javascript:if(this.min<=this.value&&this.value<=this.max){{document.location='{2}'+this.value+'.html';}}"/>
</div>
<br><br>
"""

data = lambda: dict([
    (f"*_{i+1}.html", {
        __TITLE__: r"""Articles""",
        __HTML_TITLE__: r"""~ Articles ~""",
        __CONTENT__: "<br>\n".join(
                r"""<hr>
                <div style="margin-left:2em">
                    <h2><a class="noafter" href="%s">%s</a></h2>
                    <span style="color:gray">Tags: <span style="color:blue"><b>%s</b></span></span>
                    <br><br>
                    <div class="time"></div><span><span style="color:gray">Time: </span><b>%s</b></span>
                </div>
                """ % parse_info(entries[j], import2(os.path.join(tales, entries[j]), encoding = 'utf-8').info()) for j in range(i, min(len(entries), i+interval))
            ) + tail.format(i // interval + 1, pages, page)
        }) for i in range(0, len(entries), interval)
])
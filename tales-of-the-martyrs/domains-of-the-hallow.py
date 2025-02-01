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
    <ul class="navi">
        <li>{3}</li>
        <li><span>Page: <input class="pagination" type="number" value="{0}" max="{1}" min="1" onchange="javascript:if(this.min<=this.value&&this.value<=this.max){{document.location='{2}'+this.value+'.html';}}"/></li>
        <li>{4}</li>
    </ul>
</div>
<script type="text/javascript">
window.onkeydown = function(e)
{{
    if(e.keyCode == 37 && {0} > 1)
    {{
        document.location = '{2}'+({0}-1)+'.html';
    }}else if (e.keyCode == 39 && {0} < {1})
    {{
        document.location = '{2}'+({0}+1)+'.html';
    }}
}}
</script>
<br><br>
"""

data = lambda: dict([
    (f"*_{(idx := i//interval+1)}.html", {
        __TITLE__: r"""Contents""",
        __HTML_TITLE__: r"""~ Contents ~""",
        __CONTENT__: "<br>\n".join(
                r"""<hr>
                <div style="margin-left:2em">
                    <h2><a class="noafter" href="%s">%s</a></h2>
                    <span style="color:gray">Tags: <span style="color:blue"><b>%s</b></span></span>
                    <br><br>
                    <div class="time"></div><span><span style="color:gray">Time: </span><b>%s</b></span>
                </div>
                """ % parse_info(entries[j], import2(os.path.join(tales, entries[j]), encoding = 'utf-8').info()) for j in range(i, min(len(entries), i+interval))
            ) + tail.format(idx, pages, page, '<a class="noafter" href="%s%s.html">&lt;-</a>' % (page, idx - 1) if idx > 1 else '<span style="color:gray">&lt;-</span>', '<a class="noafter" href="%s%s.html">-&gt;</a>' % (page, idx + 1) if idx < pages else '<span style="color:gray">-&gt;</span>')
        }) for i in range(0, len(entries), interval)
])
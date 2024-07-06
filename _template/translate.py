import os

workdir = ".."
__TITLE__ = '!@#$%__TITLE__%$#@!'
__HTML_TITLE__ = '!@#$%__HTML_TITLE__%$#@!'
__CONTENT__ = '!@#$%__CONTENT__%$#@!'

class Attrs:
    def __init__(self):
        pass
    
    def __init__(self, dic):
        for key, value in dic.items():
            self[key] = value
    
    def __setitem__(self, name, value):
        super().__setattr__(name, value)

def import2(path, *args, **kwargs):
    attrs = {
        'import2': import2,
        'workdir': workdir,
        'Attrs': Attrs,
        '__TITLE__': __TITLE__,
        '__HTML_TITLE__': __HTML_TITLE__,
        '__CONTENT__': __CONTENT__
    }
    exec(open(path, *args, **kwargs).read(), attrs)
    return Attrs(attrs)

bad  = lambda *args: print('[\x1b[31;1m-\x1b[0m] ' + '\n    '.join(map(str, args)))
good = lambda *args: print('[\x1b[32;1m+\x1b[0m] ' + '\n    '.join(map(str, args)))
warn = lambda *args: print('[\x1b[33;1m!\x1b[0m] ' + '\n    '.join(map(str, args)))
info = lambda *args: print('[\x1b[34;1m*\x1b[0m] ' + '\n    '.join(map(str, args)))
stress = lambda text: f'\x1b[1;4m{text}\x1b[0m'
flagfmt = lambda flag: '\x1b[33;1m%s\x1b[0m' % ''.join(chr(x) if x in range(32,127) else '\x1b[31;1m·\x1b[33;1m' for x in flag)

read = lambda path, *args, **kwargs: open(path, 'r', *args, **kwargs).read()
write = lambda path, data, *args, **kwargs: open(path, 'w', *args, **kwargs).write(data)

template = read('template.html', encoding = 'utf-8')
disallow = [
    '_template',
    'spirit-of-mathematics'
]

for i, j, k in os.walk(".."):
    for l in k:
        check = i.split('\\')
        flag = 0
        for entry in disallow:
            if entry in check:
                flag = 1
                break
        if flag: continue
        path = os.path.join(i, l)
        stem = '\\'.join(path.split('\\')[:-1])
        name = '.'.join(path.split('\\')[-1].split('.')[:-1])
        if path.endswith(".py"):
            obj = import2(path, encoding = 'utf-8')
            data = obj.data()
            info_ = 0
            if hasattr(obj, 'info'):
                info_ = obj.info()
            for key0, value0 in data.items():
                if info_:
                    if __TITLE__ not in value0:
                        value0.update({__TITLE__: info_.title})
                    if __HTML_TITLE__ not in value0:
                        value0.update({__HTML_TITLE__: info_.title})
                    value0[__CONTENT__] += r"""<br><br><br><br><br><br><p style="color:gray">Tags: <span style="color:blue"><b>%s</b></span></p>
                    <p style="color:gray"><div class="time"></div>Time: <b>%s</b></p><br><br><br><br><br><br>""" % ('</b></span><span color="gray">, </span><span style="color:blue"><b>'.join('#%s' % tag for tag in info_.tags), info_.time)
                new_path = os.path.join(stem, key0.replace('*', name))
                info("Processing:", stress(new_path))
                html = template
                for key1, value1 in value0.items():
                    html = html.replace(key1, value1)
                write(new_path, html, encoding = 'utf-8')




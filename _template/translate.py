import os, re, pickle

workdir = ".."
__TITLE__ = '!@#$%__TITLE__%$#@!'
__HTML_TITLE__ = '!@#$%__HTML_TITLE__%$#@!'
__CONTENT__ = '!@#$%__CONTENT__%$#@!'
__LIMITED_EXPERTISE__ = '__LIMITED_EXPERTISE__'
__ASSETS__ = '__ASSETS__'
__EXERCISE__ = '__EXERCISE__'

VAL__LIMITED_EXPERTISE__ = r"""<div class="center"><p><comment>Note: The author's limited expertise in current topic may result in unclear or potentially erroneous articulations.</comment></p></div><br><br>"""
VAL__EXERCISE__ = "<comment><s>（证明留做习题）</s></comment>"

const_names = {
    '__TITLE__': __TITLE__,
    '__HTML_TITLE__': __HTML_TITLE__,
    '__CONTENT__': __CONTENT__,
    '__LIMITED_EXPERTISE__': __LIMITED_EXPERTISE__,
    '__ASSETS__': __ASSETS__,
    '__EXERCISE__': __EXERCISE__
}

def const_values(index):
    return {
        __LIMITED_EXPERTISE__: VAL__LIMITED_EXPERTISE__,
        __EXERCISE__: VAL__EXERCISE__,
        __ASSETS__: '/tales-of-the-martyrs/tales/oracle-of-namagiri/%s' % index if index else ''
    }

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
        'path': path
    }
    attrs.update(const_names)
    exec(open(path, *args, **kwargs).read(), attrs)
    return Attrs(attrs)

def needs_update(path):
    global mtime_dict
    if mtime_dict is None:
        if os.path.exists("mtime.pickle"):
            with open("mtime.pickle", "rb") as f:
                mtime_dict = pickle.load(f)
        else:
            mtime_dict = {}
    path_data = '.'.join(path.split('.')[:-1]) + '.data'
    info = os.stat(path)
    mtime = info.st_mtime
    res = mtime_dict.get(path, 0) < mtime
    mtime_dict.update({path: mtime})
    if os.path.exists(path_data):
        info_data = os.stat(path_data)
        mtime_data = info_data.st_mtime
        res = res or mtime_dict.get(path_data, 0) < mtime_data
        mtime_dict.update({path_data: mtime_data})
    return res

def save_mtime():
    with open("mtime.pickle", "wb") as f:
        pickle.dump(mtime_dict, f)

bad  = lambda *args: print('[\x1b[31;1m-\x1b[0m] ' + '\n    '.join(map(str, args)))
good = lambda *args: print('[\x1b[32;1m+\x1b[0m] ' + '\n    '.join(map(str, args)))
warn = lambda *args: print('[\x1b[33;1m!\x1b[0m] ' + '\n    '.join(map(str, args)))
info = lambda *args: print('[\x1b[34;1m*\x1b[0m] ' + '\n    '.join(map(str, args)))
stress = lambda text: f'\x1b[1;4m{text}\x1b[0m'
flagfmt = lambda flag: '\x1b[33;1m%s\x1b[0m' % ''.join(chr(x) if x in range(32,127) else '\x1b[31;1m·\x1b[33;1m' for x in flag)

read = lambda path, *args, **kwargs: open(path, 'r', *args, **kwargs).read()
write = lambda path, data, *args, **kwargs: open(path, 'w', *args, **kwargs).write(data)

mtime_dict = None

template = read('template.html', encoding = 'utf-8')
disallow = [
    '_template',
    'essence-of-the-elders',
    'oracle-of-namagiri'
]

banner = """Translation starts.    :)

"""




print(banner)

for i, j, k in os.walk(".."):
    check = i.split('\\')
    flag = 0
    for entry in disallow:
        if entry in check:
            flag = 1
            j[:] = []
            break
    if flag: continue
    if 'tales' in check:
        k = [f for f in k if f.endswith('.py')]
        k.sort(key = lambda x: int(x.split('_')[0]))
    for l in k:
        path = os.path.join(i, l)
        stem = '\\'.join(path.split('\\')[:-1])
        name = '.'.join(path.split('\\')[-1].split('.')[:-1])
        if path.endswith(".py"):
            if not needs_update(path):
                info("Skipping:", stress(path))
                continue
            info("Processing:", stress(path))
            index = int(name.split('_')[0]) if 'tales' in check else None
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
                    value0[__CONTENT__] += r"""<br><br><br><br><br><br><br><br><br><br><p style="color:gray">Tags: <span style="color:blue"><b>%s</b></span></p>
                    <p><div class="time"></div><span style="color:gray">Time: </span><b>%s</b></p><br><br><br><br><br><br>""" % ('</b></span><span color="gray">, </span><span style="color:blue"><b>'.join('#%s' % tag for tag in info_.tags), info_.time)
                value0.update(const_values(index))
                new_path = os.path.join(stem, key0.replace('*', name))
                good("Creating:", stress(new_path))
                html = template
                for key1, value1 in value0.items():
                    html = html.replace(key1, value1)
                write(new_path, html, encoding = 'utf-8')

save_mtime()


from json import dump, load
from os import remove, replace
from random import uniform
from re import sub
from time import sleep
from uuid import uuid4 as uu


def clean_str(s):
    s = sub(r'…', '...', s)
    s = sub(r'[`‘’‛⸂⸃⸌⸍⸜⸝]', "'", s)
    s = sub(r'[„“]|(\'\')|(,,)', '"', s)
    s = sub(r'\s+', ' ', s).strip()
    return s


def gen_str(length=16):
    s = ''
    for i in range(max(1, int(length/32))):
        s += str(uu()).replace('-', '') 
    lst = [s[i:i+1] for i in range(0, len(s), 1)] 
    return ''.join(lst[:length])


def dump_json(content, dest):
    pth = f'./{uu()}{uu()}.json'
    with open(pth, "w") as f:
        dump(content, f, indent=4)
    try:
        with open(pth) as f:
            q = load(f)
        replace(pth, dest)
    except:
        remove(pth)


def load_json(pth):
    with open(pth, 'r') as json_file:
        data = load(json_file)
    return data


def zzz(mn=2, mx=3):
    return sleep(round(uniform(mn, mx), 4))


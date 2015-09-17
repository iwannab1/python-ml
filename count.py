import glob
from konlpy.tag import Kkma
from konlpy import utils
from collections import Counter
import os



def writeResult(name, ext, lineset):
    with open('c:\\temp\\text\\' + name + '.' + ext, mode="w", encoding="utf8") as f1:
        for line in lineset:
            print(line, file=f1)


def getName(path):
    s = path.rfind(os.sep)
    e = path.rfind('.')
    return path[s+1:e]

def getDiv(f):
    lineSet = set()
    file = open(f,'r', encoding="utf-8")

    while 1:
        line = file.readline().strip()
        if not line:
            break
        else:
            lineSet.add(line)


    return lineSet


if __name__=='__main__':
    kkma = Kkma()
    files = glob.glob("c:\\temp\\count\\*.count")
    for f in files:
        print(f)
        writeResult(getName(f), 'count', getDiv(f))







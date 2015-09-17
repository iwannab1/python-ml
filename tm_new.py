import glob
from konlpy.tag import Kkma
from konlpy import utils
from collections import Counter
import os


def writeResult1(name, ext, dict):
    with open('c:\\temp\\text\\' + name + '.' + ext, mode="w", encoding="utf8") as f1:
        for key in dict.keys():
            print(key + ',' + '"' + dict[key] + '"', file=f1)

def writeResult(name, ext, dict, info):
    item = ['NNG' , 'NNP', 'UN', 'OL']
    with open('c:\\temp\\text\\' + name + '.' + ext, mode="w", encoding="utf8") as f2:
        for key in dict.keys():
            if key in item:
                wordlist = dict[key]
                print(key + ',' + '"' + ', '.join(wordlist) + '"', file=f2)
    nmg = dict['NNG']
    with open('c:\\temp\\text\\' + name + '.count' , mode="w", encoding="utf8") as f3:
        for word in nmg:
            print('"' + info['21'] + '","' + info['51'] + '"' + "," + word + "," + str(nmg.count(word)), file=f3)


def getTags(pos):
    dict = {}
    for word, tag in pos:
        if tag in dict:
            words = dict.get(tag)
            words.append(word)
        else:
            words = list(word)
        dict[tag] = words
    return dict

def getToken(str):
    token = ""
    arr = str.split(" ")
    cnt = len(arr)
    for i in range(cnt):
        s = arr[i]
        if len(s) > 0:
            if s[0].isalpha():
                token += s + " "

            if s[0].isdigit():
                token += s + ","
    return token

def getDiv(f):
    dict = {}
    file = open(f,'r', encoding="utf-8")
    s51 = False
    e51 = False
    s72 = False
    e72 = False

    while 1:
        line = file.readline().strip()
        if e51:
            s51 = False
        if e72:
            s72 = False
        if s51:
            if line.startswith('('):
                s51 = False
                continue
            if '51' in dict:
                str51 = dict.get('51') + getToken(line)
                dict['51'] = str51
            else:
                dict['51'] = getToken(line)
        if s72:
            if line.startswith('('):
                s72 = False
            if '72' in dict:
                str72 = dict.get('72')  + "," + line
                dict['72'] = str72
            else:
                dict['72'] = line
        if not line:
            break
        else:
            if line.startswith('(51)'):
                s51 = True
            elif line.startswith('(21)'):
                arr = line.split(" ")
                for i in range(len(arr)):
                    s = arr[i]
                    if len(s) > 0:
                        if s[0].isdigit():
                            dict['21'] = s
            elif line.startswith('(72)'):
                s72 = True

    return dict


def wordCount(name, f):
    file = open(f,'r', encoding="utf-8")
    wordcount = Counter(file.read().split())
    with open('c:\\temp\\text\\' + name + '.count', mode="w", encoding="utf8") as f:
        for item in wordcount.items():
            print(item[0] + ',' + str(item[1]), file=f)

def getName(path):
    s = path.rfind(os.sep)
    e = path.rfind('.')
    return path[s+1:e]

if __name__=='__main__':
    kkma = Kkma()
    files = glob.glob("c:\\temp\\text\\*.txt")
    for f in files:
        print(f)
        name = getName(f)
        info = getDiv(f)
        writeResult1(name, 'info', info)
        doc = utils.load_txt(f).read()
        pos = Kkma().pos(doc)
        writeResult(name, 'pos', getTags(pos), info)







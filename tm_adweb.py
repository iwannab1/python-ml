import glob
from konlpy.tag import Kkma
from konlpy import utils
from collections import Counter
import os, re
import threading
import time

def writePosResult(name, ext, head, dict, dictset, info):
    item = ['NNG', 'VA']
    with open('d:\\adweb\\' + name + '_pos.' + ext, mode="a", encoding="utf8") as f2:
        print(head, file=f2)
        for key in dict.keys():
            if key in item:
                wordset = dictset[key]
                words = dict[key]
                for w in wordset:
                    print(info + w + '\t' + str(words.count(w)), file=f2)

def writeResult(name, ext, head, wordcount, info):
    with open('d:\\adweb\\' + name + '.' + ext, mode="a", encoding="utf8") as f2:
        for item in wordcount.items():
            pure = ''.join(e for e in item[0] if e.isalnum())
            print(info + pure + '\t' + str(item[1]), file=f2)


def getTags(pos):
    dict = {}
    dictset = {}
    for word, tag in pos:
        if tag in dict:
            words = dict.get(tag)
            words.append(word)
            wordset = dictset.get(tag)
            wordset.add(word)
        else:
            words = list(word)
            wordset = set(word)
        dict[tag] = words
        dictset[tag] = wordset
    return dict, dictset


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
    file = open(f, 'r', encoding="utf-8")
    body = ''
    info = ''
    while 1:
        line = file.readline().strip()
        if not line:
            break
        else:
            if line.startswith('본문 : '):
                body = line.replace("본문 : ", "")
            else:
                info += line[line.index(":") + 1:] + "\t"

    return body, info


def getName(path):
    s = path.rfind(os.sep)
    e = path.rfind('.')
    return path[s + 1:e]

def run(id):
    files = glob.glob("d:\\" + id + "\\*.txt")
    body = ""
    for f in files:
        print(f)
        body, info = getDiv(f)
        writeResult(id, 'csv', "", Counter(body.split()), info)

def runpos(kkma, id):
    files = glob.glob("d:\\" + id + "\\*.txt")
    for f in files:
        print(f)
        body, info = getDiv(f)
        pos = kkma.pos(body)
        dict, dictset = getTags(pos)
        writePosResult(id, 'csv', "", dict, dictset, info)



if __name__ == '__main__':

    # run("news")
    # run("blog")
    # run("kin")
    # run("twitter")
    # run("facebook")
    # run("agora")

    kkma = Kkma()
    agora = threading.Thread(target=runpos(kkma, "agora"))
    agora.start()
    facebook = threading.Thread(target=runpos(kkma, "facebook"))
    facebook.start()
    twitter = threading.Thread(target=runpos(kkma, "twitter"))
    twitter.start()
    kin = threading.Thread(target=runpos(kkma, "kin"))
    kin.start()
    blog = threading.Thread(target=runpos(kkma, "blog"))
    blog.start()
    news = threading.Thread(target=runpos(kkma, "news"))
    news.start()




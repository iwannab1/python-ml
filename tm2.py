import glob

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
                token += s + " |"
    return token


def getDiv(name, f):
    file = open(f,'r', encoding="utf-8")
    bk = False
    while 1:
        line = file.readline()
        if bk:
            print(name + ":" + getToken(line))
            break
        if not line:
            break
        else:
            if "국제특허분류" in line:
                bk = True

def getName(path):
    s = path.rfind(os.sep)
    e = path.rfind('.')
    return path[s+1:e]

if __name__=='__main__':
    files = glob.glob("c:\\temp\\text\\*.txt")
    for f in files:
        name = getName(f)
        getDiv(name, f)






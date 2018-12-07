import hashlib
import os, sys


def CalcSha1(filepath):
    with open(filepath, 'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        print(hash)
        return hash


def CalcMD5(filepath):
    f = open(filepath, 'rb')
    md5obj = hashlib.md5()
    md5obj.update(f.read())
    hash = md5obj.hexdigest()
    f.close()
    print(hash)
    name ="md5.txt"
    f = open(name, 'a', encoding="UTF-8")
    f.write(hash+"\n")
    f.close()
    return hash


if __name__ == "__main__":
    hashfile = "./DouyuSpiderV2.exe"
    CalcMD5(hashfile)



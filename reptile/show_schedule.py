# coding=utf-8
# 本文实例讲述了python下载文件时显示下载进度的方法。
# 将这段代码放入你的脚本中，类似：urllib.urlretrieve(getFile, saveFile, reporthook=report)
# 第三个参数如下面的函数定义report，urlretrieve下载文件时会实时回调report函数，显示下载进度

import sys
import urllib.request as urllib
from urllib import request, parse

getFile = []
saveFile = []


def report(count, blockSize, totalSize):
    percent = int(count * blockSize * 100 / totalSize)
    sys.stdout.write("\r%d%%" % percent + ' complete')
    sys.stdout.flush()


urllib.urlretrieve(getFile, saveFile, reporthook=report)

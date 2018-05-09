import re
import os
import urllib.request as urllib
from urllib import request, parse
import sys


def getHtml(url):
    head = {}
    # 写入User Agent信息
    head[
        'User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ' \
                        'WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729;' \
                        ' .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'
    # 创建Request对象
    req = request.Request(url, headers=head)
    page = request.urlopen(req)
    html = page.read()
    html = html.decode('utf-8')
    return html


def getImage(html):
    # 根据正则表达式匹配图片的地址，但是这个网址里面只有缩略图，所以这里匹配的是缩略图的名字
    pp = re.compile(r'img src=(".*t1.jpg)"')
    imglist = re.findall(pp, html)
    # 存储图片的下载地址
    newimglist = []
    # 存储图片的名字
    imgnamelist = []
    for index in range(len(imglist)):
        # 单独取出来图片的名字(不带.jpg)
        img_name = imglist[index].split("/")[-1][:-7]
        imgnamelist.append(img_name)
        new_name = "http://wallpaperswide.com/download/" + str(img_name) + "-wallpaper-1920x1080.jpg"
        newimglist.append(new_name)
    print(imglist)

    # 定义一个report,来作为urlretrieve的第三个参数，显示进度
    def report(count, blockSize, totalSize):
        percent = int(count * blockSize * 100 / totalSize)
        sys.stdout.write("\r%d%%" % percent + ' complete')
        sys.stdout.flush()

    x = 0
    for imgurl in newimglist:
        print('正在下载 ', imgurl)
        # 函数格式为urllib.urlretrieve(getFile, saveFile, reporthook=report)
        urllib.urlretrieve(imgurl, 'X:\jet_python\downloads/wallpaper/%s.jpg' % imgnamelist[x],
                           reporthook=report)
        print("\n")
        x += 1


urllist = []
# 下载首页中第一页到第二十页的所有壁纸
for i in range(1, 20):
    urlname = "http://wallpaperswide.com/page/" + str(i)
    urllist.append(urlname)
    html = getHtml(urlname)
    getImage(html)
    path = os.getcwd()
    print(path)

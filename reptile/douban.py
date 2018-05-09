# coding=utf-8
import urllib.request

#
# url = "http://www.douban.com/"
# # url = "https://www.qiushibaike.com/"
#
#
# #请求
# request = urllib.request.Request(url)
# #爬取结果
# response = urllib.request.urlopen(request)
# data = response.read()
# #设置解码方式
# data = data.decode("utf-8","ignore")
# print(data)

# Request()
'''
使用request（）来包装请求，再通过urlopen（）获取页面。
urllib.request.Request(url, data=None, headers={}, method=None)
request请求,它其实就是一个Request类的实例，构造时需要传入Url,Data等等的内容。
对于头部的数据
User-Agent ：这个头部可以携带如下几条信息：浏览器名和版本号、操作系统名和版本号、默认语言
Referer：可以用来防止盗链，有一些网站图片显示来源http://***.com，就是检查Referer来鉴定的
Connection：表示连接状态，记录Session的状态。
'''

# urlopen()
'''
urlopen(url, data, timeout)
第一个参数url即为URL，第二个参数data是访问URL时要传送的数据，第三个timeout是设置超时时间。
第二三个参数是可以不传送的，data默认为空None，timeout默认为 socket._GLOBAL_DEFAULT_TIMEOUT
第一个参数URL是必须要传送的，在这个例子里面我们传送了百度的URL，执行urlopen方法之后，返回一个response对象，返回信息便保存在这里面。
response对象有以下几个方法：
read():可以返回获取到的网页内容。
info()：返回HTTPMessage对象，表示远程服务器返回的头信息
geturl()：返回请求的url
getcode()：返回Http状态码。
如果是http请求，那么：
100：继续  客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。
101：转换协议  在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。
102：继续处理   由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。
200：请求成功      处理方式：获得响应的内容，进行处理
201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到    处理方式：爬虫中不会遇到
202：请求被接受，但处理尚未完成    处理方式：阻塞等待
204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。    处理方式：丢弃
300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。    处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源    处理方式：重定向到分配的URL
302：请求到的资源在一个不同的URL处临时保存     处理方式：重定向到临时的URL
304：请求的资源未更新     处理方式：丢弃
400：非法请求     处理方式：丢弃
401：未授权     处理方式：丢弃
403：禁止     处理方式：丢弃
404：没有找到     处理方式：丢弃
500：服务器内部错误  服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器端的源代码出现错误时出现。
501：服务器无法识别  服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。
502：错误网关  作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
503：服务出错   由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。
'''

# post和get数据传送
'''
两者最重要的区别是GET方式是直接以链接形式访问，链接中包含了所有的参数，当然如果包含了密码的话是一种不安全的选择，
不过你可以直观地看到自己提交了什么内容。POST则不会在网址上显示所有的参数，
urlopen（）的data参数默认为None，当data参数不为空的时候，urlopen（）提交方式为Post。
'''
import urllib
import urllib.request
import urllib.parse

values = {"username": "1016903103@qq.com", "password": "XXXX"}
data = urllib.parse.urlencode(values).encode('utf-8')
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url, data)
response = urllib.request.urlopen(request)
print(response.read())

# urlencode()
'''
主要作用就是将url附上要提交的数据。 
经过urlencode（）转换后的data数据为?first=true?pn=1?kd=Python，最后提交的url为

https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdnfirst=true?pn=1?kd=Python

Post的数据必须是bytes或者iterable of bytes，不能是str，因此需要进行encode()编码
'''

# 使用代理
'''
urllib.request.ProxyHandler(proxies=None)
当需要抓取的网站设置了访问限制，这时就需要用到代理来抓取数据。
'''

from urllib import request, parse

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'Python'
}
proxy = request.ProxyHandler({'http': '5.22.195.215:80'})  # 设置proxy
opener = request.build_opener(proxy)  # 挂载opener
request.install_opener(opener)  # 安装opener
data = parse.urlencode(data).encode('utf-8')
page = opener.open(url, data).read()
page = page.decode('utf-8')

# 设置User Agent方法
from urllib import request

if __name__ == "__main__":
    # 以CSDN为例，CSDN不更改User Agent是无法访问的
    url = 'http://www.csdn.net/'
    head = {}
    # 写入User Agent信息
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    # 创建Request对象
    req = request.Request(url, headers=head)
    # 传入创建好的Request对象
    response = request.urlopen(req)
    # 读取响应信息并解码
    html = response.read().decode('utf-8')
    # 打印信息
    print(html)

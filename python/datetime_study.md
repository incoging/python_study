### datetime模块
datetime模块是date和time模块的合集。有5个类
* datetime.date: 表示日期
* datetime.datetime: 表示日期时间的类
* datetime.time: 表示时间的类
* datetime.timedelta: 表示时间间隔，即两个时间点的间隔
* datetime.tzinfo: 时区的相关信息

#### datetime.date
datetime 是一个模板，datetime.date是模板中的一个类。<br/>
给定年月日，来初始化一个date类实例
```
# 返回year-month-day
datetime.date(year, month, day)  # month,day 直接写数字，前面不用加 0 
```
date类的一些方法：<br/>
##### datetime.date.ctime(),返回格式如 Sun Apr 16 00:00:00 2017
```
now = datetime.date(1998, 12, 1)
now_ctime = now.ctime()
print(now)
print(now_ctime)
```
##### datetime.date.fromtimestamp(timestamp)
根据给定的时间戮，返回一个date对象；datetime.date.today()作用相同.
讲讲时间戳的定义：从格林威治时间1970年01月01日00时00分00秒起至现在的总秒数。
看一个易错点：
```
>>> int((datetime(2016, 5, 21, 0, 0, 0) -  datetime(1970, 1, 1, 0, 0, 0)).total_seconds())  
1463788800
# 获取秒数后再将时间还原
 >>> datetime.fromtimestamp(1463788800)  
datetime.datetime(2016, 5, 21, 8, 0)  
```
发现时间不对，问题在于：“1970年01月01日00时00分00秒”指的是格林威治时间，
那么对应的北京时间应该是“1970年01月01日08时00分00秒”。
所以正确计算当前时区时间的时间戳时应该是：
拿“当前时区的时间”减去“当前时区在格林威治时间1970年01月01日00时00分00秒时的时间”。
```
>>> int((datetime(2016, 5, 21, 0, 0, 0) -  datetime(1970, 1, 1, 8, 0, 0)).total_seconds())  
1463760000 
>>> datetime.fromtimestamp(1463760000)  
datetime.datetime(2016, 5, 21, 0, 0) 
```
> datetime.date.fromtimestamp()的使用
```
new_time = datetime.date.fromtimestamp(100000000.0)
print(new_time)

output:
1973-03-03
```
##### datetime.date.isocalendar()
返回格式如(year, week number, weekday.)的元组,(2017, 15, 6)
```
import datetime
now = datetime.date(1998, 2, 1)
now_isocalendar = now.isocalendar()
print(now)
print(now_isocalendar)

output:
(1998, 5, 7)
```

##### datetime.date.isoformat()
返回格式如YYYY-MM-DD
```
import datetime
now = datetime.date(1998, 2, 1)
now_isofromat = now.isoformat()
print(now)
print(now_isofromat)

output:
1998-02-01
```

##### datetime.date.isoweekday()
返回给定日期的星期（0-6），星期一=1，星期日=7
```
import datetime
now = datetime.date(1998, 2, 1)
now_isoweekday = now.isoweekday()
print(now)
print(now_isoweekday)

output：
7
```
##### datetime.date.strftime(format)
把日期时间按照给定的format进行格式化。
```
import datetime
now = datetime.date(1998, 2, 1)
now_strftime = now.strftime("%Y!%m!%d %H:%M:%S")
print(now)
print(now_strftime)

output:
1998-02-01
1998!02!01 00:00:00
```
> strftime参数

%y 两位数的年份表示（00-99）

%Y 四位数的年份表示（000-9999）

%m 月份（01-12）

%d 月内中的一天（0-31）

%H 24小时制小时数（0-23）

%I 12小时制小时数（01-12）

%M 分钟数（00=59）

%S 秒（00-59）

 

%a 本地简化星期名称

%A 本地完整星期名称

%b 本地简化的月份名称

%B 本地完整的月份名称

%c 本地相应的日期表示和时间表示

%j 年内的一天（001-366）

%p 本地A.M.或P.M.的等价符

%U 一年中的星期数（00-53）星期天为星期的开始

%w 星期（0-6），星期天为星期的开始

%W 一年中的星期数（00-53）星期一为星期的开始

%x 本地相应的日期表示

%X 本地相应的时间表示

%Z 当前时区的名称

%% %号本身

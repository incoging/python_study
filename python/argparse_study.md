### argparse
argparse 模块对命令行进行解析

创建一个ArgumentParser实例
```
import argparse
parser = argparse.ArgumentParser()
```

```
class ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True)
```
* prog: 文件名，默认为sys.argv[0]，用来在help信息中描述程序的名字
* usage: 描述程序用途的字符串
* description: help信息前显示的信息
* epilog: help信息之后显示的信息

```
>>> parser = argparse.ArgumentParser(prog='my - program', usage='%(prog)s [options] usage',description = 'my - description',epilog = 'my - epilog')
>>> parser.print_help()
usage: my - program [options] usage

my - description

optional arguments:
  -h, --help  show this help message and exit

my - epilog
```
* parents ：由ArgumentParser对象组成的列表，它们的arguments选项会被包含到新ArgumentParser对象中。(类似于继承)

* formatter_class ：help信息输出的格式，为了美观…

* prefix_chars ：参数前缀，默认为"-"(最好不要修改)

```
>>> parser = argparse.ArgumentParser(prefix_chars='+')
>>> parser.add_argument('+x')
>>> parser.add_argument('++y')
>>> parser.parse_args('+x 1 ++y 2'.split())
Namespace(x='1', y='2')
>>> parser.parse_args('-x 2'.split())
usage: [+h] [+x X] [++y Y]
: error: unrecognized arguments: -x 2
```

* fromfile_prefix_chars ：前缀字符，放在文件名之前

```
>>> with open('args.txt', 'w') as fp:
...    fp.write('-f\nbar')
>>> parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
>>> parser.add_argument('-f')
>>> parser.parse_args(['-f', 'tmp', '@args.txt'])
Namespace(f='bar')
```
当参数过多时，可以将参数放到文件中读取，例子中parser.parse_args([‘-f’, ‘foo’, ‘@args.txt’])
解析时会从文件args.txt读取，相当于 [‘-f’, ‘foo’, ‘-f’, ‘bar’]

* conflict_handler ：解决冲突的策略，默认情况下冲突会发生错误，(最好不要修改)
```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo', help='old foo help')
>>> parser.add_argument('--foo', help='new foo help')
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo
```
* add_help ：是否增加-h/-help选项 (默认为True)，一般help信息都是必须的。设为False时，help信息里面不再显示-h –help信息

* argument_default： - (default: None)设置一个全局的选项的缺省值，一般每个选项单独设置，基本没用

##### 添加参数选项 - add_argument

```
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```
name or flags ：参数有两种，可选参数和位置参数。

1.添加可选参数
```
>>> parser.add_argument('-f', '--foo')
```

2.添加位置参数
```
>>> parser.add_argument('bar')
```

parse_args()运行时，默认会用’-‘来认证可选参数，剩下的即为位置参数。
```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('name')
>>> parser.add_argument('-a', '--age')
>>> parser.parse_args(['xiaoming'])
Namespace(age=None, name='xiaoming')
>>> parser.parse_args(['xiaoming','-a','123'])
Namespace(age='123', name='xiaoming')
>>> parser.parse_args(['-a','123'])
usage: [-h] [-a AGE] name
: error: too few arguments
```
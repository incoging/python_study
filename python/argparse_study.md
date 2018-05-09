### argparse
argparse ģ��������н��н���

����һ��ArgumentParserʵ��
```
import argparse
parser = argparse.ArgumentParser()
```

```
class ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True)
```
* prog: �ļ�����Ĭ��Ϊsys.argv[0]��������help��Ϣ���������������
* usage: ����������;���ַ���
* description: help��Ϣǰ��ʾ����Ϣ
* epilog: help��Ϣ֮����ʾ����Ϣ

```
>>> parser = argparse.ArgumentParser(prog='my - program', usage='%(prog)s [options] usage',description = 'my - description',epilog = 'my - epilog')
>>> parser.print_help()
usage: my - program [options] usage

my - description

optional arguments:
  -h, --help  show this help message and exit

my - epilog
```
* parents ����ArgumentParser������ɵ��б����ǵ�argumentsѡ��ᱻ��������ArgumentParser�����С�(�����ڼ̳�)

* formatter_class ��help��Ϣ����ĸ�ʽ��Ϊ�����ۡ�

* prefix_chars ������ǰ׺��Ĭ��Ϊ"-"(��ò�Ҫ�޸�)

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

* fromfile_prefix_chars ��ǰ׺�ַ��������ļ���֮ǰ

```
>>> with open('args.txt', 'w') as fp:
...    fp.write('-f\nbar')
>>> parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
>>> parser.add_argument('-f')
>>> parser.parse_args(['-f', 'tmp', '@args.txt'])
Namespace(f='bar')
```
����������ʱ�����Խ������ŵ��ļ��ж�ȡ��������parser.parse_args([��-f��, ��foo��, ��@args.txt��])
����ʱ����ļ�args.txt��ȡ���൱�� [��-f��, ��foo��, ��-f��, ��bar��]

* conflict_handler �������ͻ�Ĳ��ԣ�Ĭ������³�ͻ�ᷢ������(��ò�Ҫ�޸�)
```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo', help='old foo help')
>>> parser.add_argument('--foo', help='new foo help')
Traceback (most recent call last):
 ..
ArgumentError: argument --foo: conflicting option string(s): --foo
```
* add_help ���Ƿ�����-h/-helpѡ�� (Ĭ��ΪTrue)��һ��help��Ϣ���Ǳ���ġ���ΪFalseʱ��help��Ϣ���治����ʾ-h �Chelp��Ϣ

* argument_default�� - (default: None)����һ��ȫ�ֵ�ѡ���ȱʡֵ��һ��ÿ��ѡ������ã�����û��

##### ��Ӳ���ѡ�� - add_argument

```
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
```
name or flags �����������֣���ѡ������λ�ò�����

1.��ӿ�ѡ����
```
>>> parser.add_argument('-f', '--foo')
```

2.���λ�ò���
```
>>> parser.add_argument('bar')
```

parse_args()����ʱ��Ĭ�ϻ��á�-������֤��ѡ������ʣ�µļ�Ϊλ�ò�����
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
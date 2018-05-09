# coding=utf-8
# 这个文档主要介绍json在python中的应用
import json

# json.dumps
# 此函数将Python对象编码成JSON字符串
'''
语法：
json.dumps(obj, skipkeys = False, ensure_ascii = True, check_circular = True, allow_nan = True, 
           cls = None, indent = None, separators = None, encoding = "utf=8", default = None, 
           sort_keys = False, **kw)
skipkeys:如果``skipkeys``是真的，那么``dict``键不是
    基本类型（``str``，``int``，``float``，``bool``，``None`` ）将被跳过，而不是提出一个“TypeError”。
ensure_ascii:如果``ensure_ascii``为false，那么返回值可以包含非ASCII字符，如果它们出现在“obj”中的字符串中。
    否则，所有这些字符都将以JSON字符串进行转义。
check_circular:如果``check_circular``为false，那么容器类型的循环引用检查将被跳过，
    循环引用将导致“溢出错误”（或更坏）。
allow_nan:如果``allow_nan``是假的，那么这将是一个``ValueError``序列化
    超出范围``float``值（``nan``，``inf``，``-inf``） 严格遵守JSON规范，
    而不是使用JavaScript等价物（“NaN”，“Infinity”，“-Infinity”）。
indent:如果``indent``是一个非负整数，那么JSON数组元素和对象成员就会用这个缩进级别打印出来。
    缩进级别0将仅插入换行符。 “无”是最紧凑的表示。
separators:如果指定，``separatorators``应该是``（item_separator，key_separator）``tuple。
    默认是``（'，'，'：'）``如果* indent *是``None``和``（'，'，'：'）`` 要获得最紧凑的JSON表示，
    您应该指定`（'，'，'：'）``来消除空格。
default:``default（obj）``是一个函数，它应该返回一个可序列化的obj版本或者引发TypeError。
    默认值只是引发TypeError。
sort_keys:如果* sort_keys *是``True``（默认：``False``），那么字典的输出将按键排序。
要使用自定义的“JSONEncoder”子类（例如覆盖``.default（）''方法来序列化其他类型的子类），
    用``cls`` kwarg指定它 否则使用“JSON编码器”。
'''

data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4}]
json1 = json.dumps(data)
print(json1)
# 使用参数让JSON数据格式化输出：
json2 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
print(json2)

test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
json_str = json.dumps(test_dict, indent=4)
print(json_str)

# 原始类型向json类型转化对照表：
'''
Python	              JSON
dict	             object
list, tuple	       array
str, unicode	      string
int, long, float	   number
True	              true
False	              false
None	              null
'''

# json.loads
# 用于解码JSON数据，该函数返回python字段的数据类型
jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
text = json.loads(jsonData)
print(text)
'''
语法：
loads(s, encoding=None, cls=None, object_hook=None, parse_float=None,
        parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
object_hook:``object_hook``是一个可选的函数，它将被任意对象字面解码的结果（一个``dict``）调用。 
    将使用`object_hook``的返回值，而不是``dict``。 此功能可用于实现自定义解码器（例如JSON-RPC类提示）。
object_pairs_hook:``object_pairs_hook``是一个可选的函数，它将被任意对象的结果使用对数列表进行解码。 
    将使用`object_pairs_hook``的返回值，而不是``dict``。 
该功能可用于实现依赖于键和值对被解码的顺序的定制解码器（例如，collections.OrderedDict将记住插入的顺序）。
    如果`object_hook`也被定义，``object_pairs_hook``优先。
parse_float:如果指定，将使用要解码的每个JSON float的字符串进行调用。 默认情况下，这相当于float（num_str）。
    这可以用于使用另一个数据类型或解析器的JSON浮点数（例如decimal.Decimal）。
parse_int:（如果指定的话）将被调用与要解码的每个JSON int的字符串。 默认情况下，这相当于int（num_str）。
    这可以用于为JSON整数使用另一个数据类型或解析器（例如float）。
parse_constant:如果指定，将使用以下字符串之一调用：-Infinity，Infinity，NaN，null，true，false。 
    如果遇到无效的JSON数字，则可以用于引发异常。

'''
# json 类型转换到 python 的类型对照表：
'''

JSON	             Python
object              	dict
array	              list
string	             unicode
number (int)	    int, long
number (real)      	float
true	              True
false              	False
null	              None
'''

# json.dump
# 将数据写入到json文件中
with open("X:\jet_python\study\study_json\json_data/json_demo.json", "w") as f:
    json.dump(text, f)
    print(text)
    print("加载入文件完成...")

# json.load
# 把文件打开，并把字符串变换为数据类型
with open("X:\jet_python\study\study_json\json_data/json_demo.json", 'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
load_dict['a'] = [8200, {1: [['Python', 81], ['shirt', 300]]}]
print(load_dict)

with open("X:\jet_python\study\study_json\json_data/json_demo.json", "w") as dump_f:
    json.dump(load_dict, dump_f)

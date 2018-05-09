# coding=utf-8
# 这篇文档主要讲述一个文件夹下的路径分割和文件名利用问题
import os
import glob

# os.walk
# path1 = "X:\jet_python\study\study_python\python_data_study"
# allinf, files = os.walk(path1)
# print(allinf)      #('X:\\jet_python\\lab\\data\\inputimg', ['result'], ['0_10.bmp', '0_11.bmp', '0_12.bmp', '0_13.bmp', '0_8.bmp', '0_9.bmp', 'json_demo.json'])
# print(files)       #('X:\\jet_python\\lab\\data\\inputimg\\result', [], ['0_9.jpg'])
'''
Notice: 如果路径不对的话，将什么都不输出，也不报错
allinf接收到这个path下的所有信息，前面是路径，中间一个是文件夹，后面的是一个一个的文件
files接收到的是一个path下一层的文件夹信息，并显示里面的文件，中间有一个空的列表,表示里面没有文件夹
'''

# path2 = "X:\jet_python\study\study_python\python_data_study"
# for root, dirs, files in  os.walk(path2):
#     print(root)
#     print(dirs)
#     print(files)
'''
Notice: 如果路径不对的话，将什么都不输出，也不报错
output:
X:\jet_python\lab\data\inputimg
['result']
['0_10.bmp', '0_11.bmp', '0_12.bmp', '0_13.bmp', '0_8.bmp', '0_9.bmp', 'json_demo.json']
X:\jet_python\lab\data\inputimg\result
[]
['0_9.jpg']

由以上可以看出，第一次的for循环（即for循环第一次遍历），显示出了path目录下的root目录，文件夹信息，文件信息。
第二次的for循环，相当于进入了path的下一层(即更深的一层。)，显示了这一层的root目录，文件夹信息，文件信息。
即有外层向里层依次输出root目录，文件夹信息，文件信息。
若将os.walk(topdown=False)参数topdown设为false,则将会从最里层的子目录开始遍历，到最外层结束。
'''

# os.path.splitext()
path3 = "X:\jet_python\study\study_python\st_python_data\*.jpg"
for infiles in glob.glob(path3):
    f, ext = os.path.splitext(infiles)
    print(f)
    print(ext)
'''
X:\jet_python\study\study_python\st_python_data\first
.jpg
X:\jet_python\study\study_python\st_python_data\fourth
.jpg
X:\jet_python\study\study_python\st_python_data\sec
.jpg
X:\jet_python\study\study_python\st_python_data\third
.jpg

即glob.glob会搜索出全部匹配的文件，os.path.splitext(path)会依据最后的一个“.”来把路径划分为两段，
前一段赋给f,后面的“.jpg”赋给ext
'''

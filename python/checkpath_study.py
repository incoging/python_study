# coding = utf-8
# 在命令窗口查看Python路径


# 方法一：
# 在命令窗口直接输入：
# python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"

"""
output:
C:\Python3\Lib\site-packages
"""


# 方法二：
# 在命令窗口直接输入：
# python3 -c "import os; print(os.__file__)"
'''
output:
C:\Python27\lib\os.pyc
'''

# 方法三：
# 在命令窗口直接输入：
# python3 -c "import sys; print(sys.executable)"
'''
output:
C:\Python3\python3.exe
'''

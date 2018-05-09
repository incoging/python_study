# coding=utf-8
# os模块主要用于处理文件和目录。
import os

# os.access()方法
"""
os.access(path, mode)
path -- 要用来检测是否有访问权限的路径
mode -- 测试的模式，可以为以下参数
    os.F_OK : 测试path是否存在
    os.R_OK : 测试path是否可读
    os.W_OK : 测试path是否可写
    os.X_OK : 测试path是否可执行

返回值： 如果允许访问返回True，否则返回False。
"""
# 假定 ./foo.txt 文件存在，并有读写权限

ret = os.access("foo.txt", os.F_OK)
print("F_OK - 返回值 %s" % ret)

ret = os.access("./foo.txt", os.R_OK)
print("R_OK - 返回值 %s" % ret)

ret = os.access("./foo.txt", os.W_OK)
print("W_OK - 返回值 %s" % ret)

ret = os.access("./foo.txt", os.X_OK)
print("X_OK - 返回值 %s" % ret)

"""
output:
F_OK - 返回值 True
R_OK - 返回值 True
W_OK - 返回值 True
X_OK - 返回值 True
"""

# os.chdir()
"""
os.chdir(path)
path -- 要切换到的新路径

返回值：如果允许返回True，否则返回False   X:\jet_python\study\study_python\python
"""

path = "/tmp"

# 查看当前工作目录
current = os.getcwd()
print("当前工作目录为 %s" % current)

# 修改当前工作目录
os.chdir(path)

# 查看当前的工作目录
current = os.getcwd()

print("目录修改成功，当前目录为： %s" % current)

def os_demo():

    # 执行命令
    dirs = os.popen("dir").read()
    print(dirs)

    # 打印目录树
    dirs_info = os.scandir()
    for info in dirs_info:
        print("文件名: {}, 路径: {}, inode: {}, 文件夹? {}, 文件? {}, 链接? {}".format(info.name, info.path, info.inode(), info.is_dir(), info.is_file(), info.is_symlink()))
        stats = info.stat()
        print(">>> 访问时间: {}, 修改时间: {}, 模式修改时间: {}, 大小: {}".format(stats.st_atime, stats.st_ctime, stats.st_mtime, stats.st_size))


import signal


def os_func():
    '''
    操作系统模块
        该模块下的方法,对各个版本的兼容不明确,须谨慎使用.
        测试版本: Python:3.6.1   Windows:Windows10,64bit
    '''

    # === 系统 ===
    strs = os.name  # 当前系统: Linux'posix' / Windows'nt' / 'ce' / 'java'
    strs = os.sep  # 分隔符 \\ (windows:\\ linux:/)
    strs = os.pathsep  # path变量分隔符 ; (windows:; linux::)
    strs = os.linesep  # 换行分隔符 \r\n (windows:/r/n linux:\n)
    dics = os.environ  # 查看系统环境变量(字典)
    strs = os.getenv("Path", default=-1)  # 读取环境变量, 没有返回None
    os.putenv("Path", "C:\\python")  # 添加环境变量  (windows无效)
    os.unsetenv("Path")  # 删除环境变量  (windows不可用)
    strs = os.getlogin()  # 当前登录的用户名
    num = os.getpid()  # 当前进程PID
    num = os.system("cmd")  # 执行操作系统命令, 返回0/1(0执行正确;1执行错误)
    strs = os.popen("dir").read()  # 执行系统命令,并去读结果
    tups = os.times()  # 当前进程时间(user用户 / system系统 / children_user子用户(windews=0) / children_system子系统(windews=0) / elapsed过去时间)
    bytes = os.urandom(10)  # n字节用以加密的随机字符
    num = os.cpu_count()  # CUP数量



    # === 进程 ===
    os.abort()  # 结束进程
    # execl(file, *args) / execle / execlp / execlpe / execv / execve / execvp / execvpe // 运行新程序替换当前进程
    os.execl(r"C:\python", 'python', 'hello.py', 'i')  # (windows执行失败)
    os._exit(0)  # 退出
    os.kill(8480, signal.SIGTERM) # (系统) 终止进程(需要导入:signal) SIGINT (终止进程) / SIGTERM (终止进程) / SIGKILL (终止进程) / SIGALRM (闹钟信号)



    # === 文件 / 文件夹 ===
    strs = os.getcwd()  # 当前路径
    bytes = os.getcwdb()  # 当前路径
    os.chdir(r"C:\Windows")  # 切换路径
    strs = os.curdir # 当前目录 .
    strs = os.pardir  # 上级目录 ..
    strs = os.sep  # 路径分隔符 ('/' or '\\')
    bytes = os.fsencode(r"C:\c.obj")  # (编码) 文件路径字符串转为bytes类型 => b'C:\\c.obj'
    strs = os.fsdecode(b"C:\c.obj")  # (解码) 文件路径转为strs类型 => 'C:\\c.obj'
    # chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
    os.chmod(r"C:\python\hello.py", 777)  # 修改模式
    os.link("file.txt", "file.txt.link")  # 创建硬链接
    os.symlink("file.txt", "file.txt.link")  # 创建软链接 (windows执行失败)
    lists = os.listdir()  # 所有文件和文件夹(列表) ".""..""D:"
    # lstat(path, *, dir_fd=None)
    tups = os.lstat(r"C:\c.obj")  # 状态信息列表
    boolean = os.access(r"C:\c.obj", os.F_OK)   # (文件/文件夹) 权限测试 (mode: F_OK存在? / R_OK可读? / W_OK可写? / X_OK可执行?)
    # scandir(path='.')  // DirEntry迭代器, 文件目录
    lists = os.scandir()
    # st_atime (访问时间) / st_ctime (修改时间) / st_mtime (模式修改时间) / st_size (大小(字节bytes))
    # st_uid (用户ID) / st_gid (用户组ID)
    # st_ino (inode) / st_mode (模式) / st_dev (设备) / st_nlink (硬链接)
    # count = cpu_count() # (系统) CPU线程数(非核数)
    tups = os.stat(".")  # 获取状态信息, 返回stat_result对象
    # utime(path, times=None, *, ns=None, dir_fd=None, follow_symlinks=True) // 更新文件的访问和修改时间
    num = os.utime(r"C:\c.obj")
    # walk(top, topdown=True, onerror=None, followlinks=False) // 根目录(top)遍历目录树,返回迭代器 (dirpath, dirnames[], filenames[]).
    root, dirnames, filenames = os.walk(r"C:\python")

    os.removedirs(r"c:\python")  # 删除多个文件夹 (windews删除多个文件夹失败,单个成功)
    # mkdir(path, mode=0o777, *, dir_fd=None) // 创建单个目录, 文件夹已存在,抛 FileExistsError 异常
    os.mkdir("test")
    # makedirs(name, mode=0o777, exist_ok=False)  // 创建(多个)文件夹
    os.makedirs(r"./t1/t2/t3")
    os.rmdir("test")  # 删除单个目录

    # mknod(path, mode=0o600, device=0, *, dir_fd=None) // 创建空文件 (windows不可用)
    os.mknod("test.txt")
    # remove(path, *, dir_fd=None)
    os.remove("test.txt")  # 删除文件
    # rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
    os.rename("text.txt", "file.txt")  # 重命名
    os.renames("text.txt", "file.txt")
    # replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None) // 重命名, 存在则替换
    os.replace("text.txt", "file.txt")
    tups = os.stat(r"text.txt")  # 文件属性



    # === 文件读写 ===
    # open(path, flags, mode=0o777, *, dir_fd=None) // 打开文件 fd:文件描述符
    fd = os.open(r"C:\c.obj", os.O_RDWR | os.O_CREAT)
    readfd, writefd = os.pipe()  # 打开管道,返回读取,写入 (windows失败)
    # fdopen(fd, *args, **kwargs) // 打开  (windews写入失败,读取""字符)
    f = os.fdopen(readfd)

    os.read(fd, 150)  # 读取
    os.write(fd, "String".encode("utf-8"))  # 写入
    os.fsync(fd)  # 强行写入
    os.ftruncate(fd, 100)  # 裁剪文件
    bytes = os.lseek(fd, 10, os.SEEK_SET)  # 设置指针  SEEK_SET(0开始) SEEK_CUR(1当前位置) SEEK_END(2末尾)

    fd_temp = os.dup(fd)  # 副本
    boolean = os.isatty(fd)  # 是否是tty设备

    stat = os.fstat(fd)  # 状态信息
    strs = os.device_encoding(fd)  # 返回终端字符编码,非终端None

    os.close(fd)  # 关闭
    os.closerange(fd, fd)  # 关闭并忽略错误


    # === DirEntry ===
    for dir in os.scandir():
        strs = dir.name  # 文件名
        strs = dir.path  # 完整路径名
        num = dir.inode()  # inode编号
        boolean = dir.is_dir()  # 是否是文件夹
        boolean = dir.is_file()  # 是否是文件
        boolean = dir.is_symlink()  # 是否是链接
        tups = dir.stat()  # 状态信息的stat_result对象

# ======================================================================




def path_demo():
    path = os.getcwd()  # 获取当前目录
    print("路径: {}".format(path))

    dirname = os.path.dirname(path)  # 获取文件夹名
    print("文件夹名为: {}".format(dirname))
    drive, path_t = os.path.splitdrive(path)  # 获取盘符
    print("盘符为: {}".format(drive))




def path_func():
    '''
    操作路径的函数
    '''
    paths = [r'file.txt', r"/python/lib/hello.py", r"/python/local/text.txt", "C:/python/local", "C:/python/file.txt"]

    strs = os.path.abspath(paths[0])  # 绝对路径
    strs = os.path.basename(paths[1])  # 文件名
    strs = os.path.dirname(paths[1])  # 文件夹名
    strs = os.path.join("C:\\", r"a.txt")  # 将路径组合返回
    dirname, filename = os.path.split(paths[1])  # 分割路径 (目录 文件名)
    strs, text = os.path.splitext(paths[1])  # 分离扩展名 (前部分, 扩展名)
    drivename, pathname = os.path.splitdrive(paths[3])  # 分离目录 (盘符, 目录)

    size = os.path.getsize(paths[0])  # 文件大小
    strs = os.path.normcase(paths[1])  # 规范大小写 (修改斜杠)
    strs = os.path.normpath(paths[1])  # 规范斜杠 (修改斜杠)
    strs = os.path.realpath(paths[1])  # 规范名字 (全名)
    # relpath(paths[0], start=os.curdir)
    strs = os.path.relpath(paths[1])  # 当前路径的文件相对路径 => 'lib\\hello.py'

    boolean = os.path.exists(paths[1])  # 路径是否存在
    boolean = os.path.isabs(paths[1])  # 是否是绝对路径 (不准)
    boolean = os.path.isfile(paths[1])  # 是否是文件
    boolean = os.path.isdir(paths[1])  # 是否是文件夹
    boolean = os.path.islink(paths[1])  # 是否是软链接
    boolean = os.path.ismount("C:\\")  # 是否是根结点
    boolean = os.path.supports_unicode_filenames  # Unicode是否可用作文件名
    boolean = os.path.samefile(paths[0], paths[0])  # 是否指向同文件或目录
    boolean = os.path.sameopenfile(os.open(paths[0], 1), os.open(paths[0], 1))  # fd是否指向同一文件
    boolean = os.path.samestat(os.stat(paths[0]), os.stat(paths[0]))  # state是否指向同一文件

    time_s = os.path.getatime(paths[0])  # 获取访问时间
    time_s = os.path.getmtime(paths[0])  # 获取修改时间
    time_s = os.path.getctime(paths[0])  # 元数据修改时间

# ===================================================================================================


import pathlib

def pathlib_demo():
    path = pathlib.Path().home() / "python"

    path_iter = path.iterdir()  # 遍历目录
    for path in path_iter:
        file_bool = path.is_file

        if not file_bool:
            continue

        print(">>> {}".format(path))

        f = path.open()  # 是文件就打开读点内容
        data = f.readline()
        print(data)
        f.close()



def pathlib_func():
    '''
    适合于不同操作系统的类来对文件系统路径进行操作
    '''

    # === PurePath (纯路径) ===
    # PurePath(*pathsegments) // 系统地灵分割
    path_pure = pathlib.PurePath('hello.py')
    path_pure = pathlib.PurePath('python', 'hello.py')
    path_pure = pathlib.PurePath(pathlib.Path('python'), pathlib.Path('hello.py'))

    # PurePosixPath(*pathsegments) // 非windows文件系统路径
    # PureWindowsPath(*pathsegments) // windows文件系统路径

    # 路径是不可变哈希的, 同风格的路径是比较有序的
    pathlib.PurePosixPath('hello') == pathlib.PurePosixPath('Hello')  # => Flase (PurePosixPath分大小写)
    pathlib.PureWindowsPath('hello') == pathlib.PureWindowsPath('hello')  # => True (PureWindowsPath不分大小写)
    pathlib.PureWindowsPath('hello') in {pathlib.PureWindowsPath('Hello')}  # => True
    pathlib.PureWindowsPath('C:') < pathlib.PureWindowsPath('d:')  # => True

    # 不同风格的路径不能比较有序
    pathlib.PureWindowsPath('hello') == pathlib.PurePosixPath('hello')  # => False
    # pathlib.PureWindowsPath('hello') < pathlib.PurePosixPath('hello')

    # 运算符
    path_pure = pathlib.PurePath('c:/')
    path_pure = path_pure / 'python' / 'hello.py'  # 拼接路径

    tups = path_pure.parts  # 返回组件元组 => ('c:\\', 'python', 'hello.py')
    drive = path_pure.drive  # 盘符 => 'c:'
    root = path_pure.root  # 根目录 => '\\'
    driroot = path_pure.anchor  # 盘符 + 根目录 => 'c:\\'
    parents = path_pure.parents  # 父路径列表 parents[0] => PureWindowsPath('c:/python')
    parent = path_pure.parent   # 父路径 => PureWindowsPath('c:/python')
    name = path_pure.name  # 文件(夹)名
    suffix = path_pure.suffix  # 扩展名
    suffixs = path_pure.suffixes  # 扩展名列表
    name = path_pure.stem  # 不带后缀名的文件(夹)名 => 'hello'

    path = path_pure.as_posix()  # 以/返回路径
    path = path_pure.as_uri()  # 以file URL方式返回路径, 必须是绝对路径 => 'file:///c:/python/hello.py'
    path = path_pure.joinpath("a.txt", "b.txt")  # 拼接路径 => PureWindowsPath('c:/python/hello.py/a.txt/b.txt')
    path = path_pure.with_name("world.py")  # 更改路径文件(夹)名 => PureWindowsPath('c:/python/world.py')
    path = path_pure.with_suffix(".txt")  # 更改扩展名,没有则添加

    boolean = path_pure.match("*.py")  # 匹配通配符 (从右侧进行匹配) (大小写的区分见上方比较代码)
    boolean = path_pure.is_absolute()  # 是否是绝对路径 (/ // c:/ 开头都被认为是绝对路径)




    # === Path (具体路径) ===
    # Path(*pathsegments)
    path = pathlib.Path('hello.py')

    # PosixPath(*pathsegments)
    # WindowsPath(*pathsegments)

    path_s = path.cwd()  # 当前路径
    home = path.home()  # 用户主目录

    state = path.stat()  # 该路径的状态信息 同os.stat()
    state = path.lstat()  # 同stat(), 目标是软链接将返回软链接信息
    path.chmod(777)  # 修改权限模式 同os.chmod()
    path.lchmod(777)  # 同chmod(), 目标是软链接将更改软链接模式
    lists = path.glob(r'*.py')  # 迭代器, 所有py文件  (windows失效)
    group = path.group()  # 文件的组  (windows不可用)
    iter = path.iterdir()  # 遍历目录 (必须是目录)
    # mkdir(mode=0o777, parents=False, exist_ok=False)
    path.mkdir()  # 创建文件夹
    path.rmdir()  # 删除文件夹
    # open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)  // 打开文件
    f = path.open()
    bytes = path.read_bytes()  # 读取文件内容
    num = path.write_bytes(b"hello")  # (覆盖)写入文件内容
    # read_text(encoding=None, errors=None)
    strs = path.read_text(encoding='utf-8')
    # write_text(data, encoding=None, errors=None)
    num = path.write_text("hello")
    ow = path.owner()  # 该文件拥有者 (windows不可用)
    path.rename("new.txt")  # 重命名,目标存在则替换
    path.replace("new.txt")  # 重命名,目标存在则替换
    path_s = path.resolve()  # 绝对路径
    path.symlink_to("hello.py", target_is_directory=False)  # 创建软链接, 如果目标是目录, 则(windows下)target_is_directory=True (windows失败)
    path.unlink()  # 删除文件/文件软链接
    # touch(mode=0o666, exist_ok=True)
    path.touch()  # 创建文件

    boolean = path.exists()  # 文件(夹)是否存在
    boolean = path.is_dir()  # 是否是文件夹
    boolean = path.is_file()  # 是否是文件
    boolean = path.is_symlink()  # 是否是硬链接
    boolean = path.is_block_device()  # 是否是块设备
    boolean = path.is_char_device  # 是否是字符设备
    boolean = path.samefile(path)  # path是否是同一文件



if __name__ == "__main__":
    os_demo()
    path_demo()
    pathlib_demo()

    # os_func()
    # path_func()
    # pathlib_func()


#返回绝对路径
os.path.abspath(path)
#返回文件名
os.path.basename(path)
#返回list(多个路径)中，所有path共有的最长的路径。
os.path.commonprefix(list)
#返回文件路径
os.path.dirname(path)
#路径存在则返回True,路径损坏返回False
os.path.exists(path)
#路径存在则返回True,路径损坏也返回True
os.path.lexists
#把path中包含的"~"和"~user"转换成用户目录
os.path.expanduser(path)
#根据环境变量的值替换path中包含的”$name”和”${name}”
os.path.expandvars(path)
#返回最后一次进入此path的时间
os.path.getatime(path)
#返回在此path下最后一次修改的时间。
os.path.getmtime(path)
 #返回path的大小
os.path.getctime(path)
#返回文件大小，如果文件不存在就返回错误
os.path.getsize(path)
#判断是否为绝对路径
os.path.isabs(path)
#判断路径是否为文件
os.path.isfile(path)
#判断路径是否为目录
os.path.isdir(path)
#判断路径是否为链接
os.path.islink(path)
#判断路径是否为挂载点（）
os.path.ismount(path)
#把目录和文件名合成一个路径
# os.path.join(path1[, path2[, ...]])
#转换path的大小写和斜杠
os.path.normcase(path)
#规范path字符串形式
os.path.normpath(path)
#返回path的真实路径
os.path.realpath(path)
#从start开始计算相对路径
# os.path.relpath(path[, start])
#判断目录或文件是否相同
# os.path.samefile(path1, path2)
#判断fp1和fp2是否指向同一文件
# os.path.sameopenfile(fp1, fp2)
#判断stat tuple stat1和stat2是否指向同一个文件
# os.path.samestat(stat1, stat2)
#把路径分割成dirname和basename，返回一个元组
os.path.split(path)
#一般用在windows下，返回驱动器名和路径组成的元组
os.path.splitdrive(path)
#分割路径，返回路径名和文件扩展名的元组
os.path.splitext(path)
#把路径分割为加载点与文件
os.path.splitunc(path)
#遍历path，进入每个目录都调用visit函数，visit函数必须有3个参数(arg, dirname, names)，dirname表示当前目录的目录名，names代表当前目录下的所有文件名，args则为walk的第三个参数
# os.path.walk(path, visit, arg)
#设置是否支持unicode路径名
# os.path.supports_unicode_filenames
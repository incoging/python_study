# coding=utf-8
# Python线程
import time
import _thread
import threading
import queue

"""
线程中常用两个模块：
_thread     python3已经废弃了thread，将thread重命名为_thread
threading   推荐使用这个
"""

# 函数调用线程
"""
_thread.start_new_thread(function, arg[, kwargs])
function -- 线程函数
args -- 传递给线程函数的参数，它必须是个tuple类型。
kwargs -- 可选参数
"""

# 为线程定义一个函数
# def print_time1(thread_name, delay):
#     count = 0
#     while count < 10:
#         time.sleep(delay)
#         count += 1
#         print("%s : %s" % (thread_name, time.ctime(time.time())))
#
#
# # 创建两个线程
# try:
#     _thread.start_new_thread(print_time1, ("Thread-1: ", 2))
#     _thread.start_new_thread(print_time1, ("Thread-2", 4))
# except:
#     print("Error: 无法启动线程。")

# while 1:
#     pass
# 如果不把这里注释起来，那么下面就无法编辑，会提示 the code is unreachable,因为程序会在这里一直循环，不会执行到下面，
# 所以要把这里注释起来。

# threading比_thread模块功能多


"""
threading模块除了包含_thread模块中的所有方法外，还提供一下方法：
threading.currentThread(): 返回当前线程变量。
threading.enumerate(): 返回一个包含正在运行的线程list，正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有异曲同工之妙（即有同样的结果）
同时，threading中Thread类给出了以下方法：
run(): 用以表示线程活动的方法。
start(): 启动线程活动。
join([time]): 等待至线程中止，这阻塞调用线程直至线程的join()方法被调用中止-正常退出或者抛出去未处理的异常-或者
是可选的超时发生。
join作用：
1. 阻塞主进程，专注于执行多线程中的程序。
2. 多线程多join的情况下，依次执行各线程的join方法，前头一个结束了才能执行后面一个。
3. 无参数，则等待到该线程结束，才开始执行下一个线程的join。
4. 参数timeout为线程的阻塞时间，如 timeout=2 就是罩着这个线程2s 以后，就不管他了，继续执行下面的代码。

isAlive(): 返回线程是否活动
getName(): 返回线程名
setName(): 设置线程名
"""

# 使用threading模块创建线程
"""
我们可以通过直接从threading.Thread继承创建一个新的子类，并实例化后调用start()方法启动新线程，即它调用了
线程的run()方法。
"""

# exitFlag = 0
#
#
# class MyThread1(threading.Thread):
#     def __init__(self, thread_id, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = thread_id
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print("退出线程：" + self.name)
#
#
# def print_time(thread_name, delay, counter):
#     while counter:
#         if exitFlag:
#             thread_name.exit()
#         time.sleep(delay)
#         print("%s: %s" % (thread_name, time.ctime(time.time())))
#         counter -= 1
#
#
# # 创建新线程
# thread1 = MyThread1(1, "Thread-1", 1)
# thread2 = MyThread1(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("退出主线程")
"""
有join输出：
开始线程：Thread-1
开始线程：Thread-2
Thread-1: Tue Jan 16 20:41:09 2018
Thread-2: Tue Jan 16 20:41:10 2018
Thread-1: Tue Jan 16 20:41:10 2018
Thread-1: Tue Jan 16 20:41:11 2018
Thread-2: Tue Jan 16 20:41:12 2018
Thread-1: Tue Jan 16 20:41:12 2018
Thread-1: Tue Jan 16 20:41:13 2018
退出线程：Thread-1
Thread-2: Tue Jan 16 20:41:14 2018
Thread-2: Tue Jan 16 20:41:16 2018
Thread-2: Tue Jan 16 20:41:18 2018
退出线程：Thread-2
退出主线程

无join输出：
开始线程：Thread-1
开始线程：Thread-2
退出主线程
Thread-1: Tue Jan 16 20:41:43 2018
Thread-1: Tue Jan 16 20:41:44 2018
Thread-2: Tue Jan 16 20:41:44 2018
Thread-1: Tue Jan 16 20:41:45 2018
Thread-2: Tue Jan 16 20:41:46 2018
Thread-1: Tue Jan 16 20:41:46 2018
Thread-1: Tue Jan 16 20:41:47 2018
退出线程：Thread-1
Thread-2: Tue Jan 16 20:41:48 2018
Thread-2: Tue Jan 16 20:41:50 2018
Thread-2: Tue Jan 16 20:41:52 2018
退出线程：Thread-2
"""

# 线程同步
"""
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。如下：
多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。
考虑这样一种情况：一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表
并打印。
那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。
为了避免这种情况，引入了锁的概念。
锁有两种状态——锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；
如果已经有别的线程比如"print"获得锁定了，那么就让线程"set"暂停，也就是同步阻塞；等到线程"print"访问完毕，
释放锁以后，再让线程"set"继续。
经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。
"""

# class MyThread2(threading.Thread):
#     def __init__(self, thread_id, name, counter):
#         threading.Thread.__init__(self)
#         self.thread_id = thread_id
#         self.name = name
#         self.counter = counter
#
#     def run(self):
#         print("开启线程：" + self.name)
#         # 获取锁，用于线程同步
#         threadLock.acquire()
#         print_time3(self.name, self.counter, 3)
#         # 释放锁，开启下一个线程
#         threadLock.release()
#
#
# def print_time3(thread_name, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print("%s : %s" % (thread_name, time.ctime(time.time())))
#         counter -= 1
#
#
# threadLock = threading.Lock()
# threads = []
#
# # 创建新线程
# thread3 = MyThread2(1, "Thread-1", 1)
# thread4 = MyThread2(2, "Thread-2", 2)
#
# # 开启新线程
# thread3.start()
# thread4.start()
#
# # 添加线程到线程列表
# threads.append(thread3)
# threads.append(thread4)
#
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print("退出主线程")


# 线程优先级队列(Queue)
"""
Python的Queue模块中提供了同步的、线程安全的队列类，包括：
1.FIFO(先入先出队列Queue)
2.LIFO(后入先出队列LifoQueue)
3.优先级队列(PriorityQueue)
这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。
Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True，反之False
Queue.full() 如果队列满了，返回True，反之False
Queue.get([block[,timeout]]) 获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item)写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
"""

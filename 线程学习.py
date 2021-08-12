# #线程体
import threading
import time
# #自定义函数实现线程体
# #线程体函数
# def thread_body():
#     # 当前线程对象
#     t = threading.current_thread()
#     for n in range(5):
#         # 当前线程名字
#         print('第{0}次执行线程{1}'.format(n,t.name))
#         #线程休眠,只有当前线程休眠，其他线程才有机会执行
#         time.sleep(2)
#     print('线程{0}执行完成'.format(t.name))
#
# #主线程
# #创建线程对象t1
# t1 = threading.Thread(target=thread_body)
# #创建线程对象t2
# t2 = threading.Thread(target=thread_body,name='MyThread')
# #启动线程t1
# t1.start()
# t2.start()


#自定义线程类实现线程体
#自定义线程类，继承Thread类
class SmallThread(threading.Thread):
    #定义线程类的构造方法，name参数是线程名
    def __init__(self,name=None):
        super().__init__(name=name)
    #线程体函数
    #重写父类Tread的run()方法
    def run(self):
        #当前线程对象
        t = threading.current_thread()
        for n in range(5):
            #当前线程名
            print('第{0}次执行线程{1}'.format(n,t.name))
            #线程休眠
            time.sleep(2)
        print('线程{0}执行完成'.format(t.name))
#主线程
#创建线程对象t1
t1 = SmallThread()
t2 = SmallThread(name='mythread')
t1.start()
t2.start()


# #当前线程对象
# t = threading.current_thread()
# #当前线程名字
# print(t.name)
# #返回当前处于活动状态的线程个数
# print(threading.active_count())
# #当前主线程对象
# b = threading.main_thread()
# print(b.name)


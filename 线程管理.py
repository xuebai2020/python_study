#等待线程结束
import threading
import time

# #共享变量,多个线程都可以访问的变量
# value = []
# #线程体函数
# def thread_body():
#     #当前线程对象
#     print('t1子线程开始...')
#     for n in range(5):
#         print('t1子线程执行...')
#         #在子线程体中修改变量value的内容
#         value.append(n)
#         time.sleep(2)
#     print('t1子线程结束')
# #主线程
# print('主线程开始...')
# t1 = threading.Thread(target=thread_body)
# t1.start()
# t1.join()
# #t1线程结束，继续执行，访问并输出变量value
# print('value={0}'.format(value))
# print('主线程继续执行...')

#线程停止
#线程停止变量，控制线程结束
isrunning = True

#工作线程体执行一些任务
def workthread_body():
    #工作线程体"死循环"
    while isrunning:
        #线程开始工作
        print("工作线程体执行中")
        time.sleep(2)

#控制线程体函数，从控制台上读取指令，根据指令修改线程停止变量
def controlthread_body():
    #在线程体中修改变量isrunning，需要声明为全局变量
    global isrunning
    while isrunning:
        #从键盘输入停止指令exit
        command = input("请输入停止指令：")
        if command == 'exit':
            isrunning = False
            print("控制线程结束。")

#主线程
#创建工作线程对象workthread
workthread = threading.Thread(target=workthread_body)
workthread.start()

controlthread = threading.Thread(target=controlthread_body)
controlthread.start()
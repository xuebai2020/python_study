'''
这个网络爬虫程序每隔一段时间都会执行一次下载图片任务，
在下载任务完成后，休眠一段时间再执行。这样反复执行，
直到爬虫程序停止。
'''

import threading
import time
import urllib.request

#线程停止
#线程停止变量，控制线程结束
isrunning = True

#工作线程体执行一些任务
def workthread_body():
    #工作线程体"死循环"
    while isrunning:
        #线程开始工作
        print("工作线程执行下载任务...")
        #在工作线程中执行下载任务，这个下载任务每5秒调用一次
        download()
        time.sleep(5)
    print('工作线程结束')

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

#下载函数
def download():
    url = 'http://localhost:8080/NoteWebService/logo.png'
    req = urllib.request.Request(url)
    with urllib.request.urlopen(url) as response:
        data = response.read()
        f_name = 'download.png'
        with open(f_name,'wb') as f:
            f.write(data)
            print('文件下载成功')
#主线程
#创建工作线程对象workthread
workthread = threading.Thread(target=workthread_body)
workthread.start()

controlthread = threading.Thread(target=controlthread_body)
controlthread.start()
import logging
import threading
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops=[2,4]   #设置2s，4s

class mythread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    def run(self):
        self.func(*self.args)
'''
loop就相当于loop0、loop1，需要传入参数
nloop：用于标识当前loop处于第几个
nsec：时间，告诉这个loop循环多久
'''
def loop(nloop,nsec):
    logging.info("start loop" + str(nloop) + "at" + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + "at" + ctime())

'''
threading中自带锁
'''
def main():
    logging.info("start all at" + ctime())
    threads= []
    nloops = range(len(loops))     #根据loops判断有几个值，即处于第几个线程：第一个、第二个
    for i in nloops:
        t = mythread(loop, (i, loops[i]), loop.__name__)   #target:目标循环函数，args：参数
        threads.append(t)   #没声明一个新的线程就追加到threads
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at" + ctime())

if __name__ == '__main__' :
    main()
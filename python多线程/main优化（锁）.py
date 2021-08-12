import _thread
import logging
from time import sleep, ctime

logging.basicConfig(level=logging.INFO)

loops=[2,4]   #设置2s，4s
'''
loop就相当于loop0、loop1，需要传入参数
nloop：用于标识当前loop处于第几个
nsec：时间，告诉这个loop循环多久
lock：传入一个已经锁上的锁，当loop执行结束，会执行一个解锁操作

'''
def loop(nloop,nsec,lock):
    logging.info("start loop" + str(nloop) + "at" + ctime())
    sleep(nsec)
    logging.info("end loop" + str(nloop) + "at" + ctime())
    lock.release()  #锁释放

'''
当所有loop执行完毕，所有锁都会被解开，主线程也会结束
'''
def main():   #主函数
    logging.info("start all at" + ctime())
    locks = []   #声明一个锁的list
    nloops = range(len(loops))     #根据loops判断有几个值，即处于第几个线程：第一个、第二个
    for i in nloops:    #执行子线程
        lock = _thread.allocate_lock()      #分配一个锁
        lock.acquire()     #加锁
        locks.append(lock)      #把加锁过的锁传给locks，append不断追加给locks
    for i in nloops:     #作用：起线程
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked(): pass
    logging.info("end all at" + ctime())

if __name__ == '__main__' :
    main()
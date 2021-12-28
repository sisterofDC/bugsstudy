import os
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing import Pipe
from time import sleep
from multiprocessing import Pool
from random import random


# Queue之间的通信 和Pipe 通信 和进程池
# PID（process ID）：
# PID是程序被操作系统加载到内存成为进程后动态分配的资源。
# 每次程序执行的时候，操作系统都会重新加载，PID在每次加载的时候都是不同的。
# PPID（parent process ID）：PPID是程序的父进程号。
def putdata(queue):
    i = 0
    while True:
        sleep(1)
        b = 'putdata' + str(i)
        i = i + 1
        queue.put(b)
        print(b, os.getpid())
        if i == 10:
            break


def getdata(queue):
    print(os.getpid())
    while True:
        sleep(2)
        file = queue.get()
        print(file, os.getpid())


def pipe_function(conn):
    conn.send([42, None, 'hello'])
    conn.close()


def count(name):
    a = random()
    b = 1 * a
    sleep(b)
    print(name, b, os.getpid())


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=pipe_function, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()

    q = Queue(20)
    p1 = Process(target=putdata, args=(q,))
    p2 = Process(target=getdata, args=(q,))
    p1.start()
    p2.start()

    pool = Pool(3)
    pool.apply_async(count, args=('a',))
    pool.apply_async(count, args=('b',))
    pool.apply_async(count, args=('c',))
    pool.close()
    pool.join()

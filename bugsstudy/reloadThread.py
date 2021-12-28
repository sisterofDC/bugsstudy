import threading
import time


class Mythread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        print(threading.current_thread(), self.name)
        time.sleep(1)


# Condition
# 商品
product = 500
# 条件变量
con = threading.Condition(threading.Lock())


class Product(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global product
        while True:
            # 所有的线程锁都有一个加锁和释放锁的动作，非常类似文件的打开和关闭。在加锁后，
            # 如果线程执行过程中出现异常或者错误，没有正常的释放锁，
            # 那么其他的线程会造到致命性的影响。
            # 通过with上下文管理器，可以确保锁被正常释放，其格式如下：
            with con:
                if product < 400:
                    product = product + 50
                    print(product)
                    time.sleep(1)
                    con.notify()
                    # 通知其他进程


class Consumer(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global product
        while True:
            with con:
                product = product - 200
                print(product)
                time.sleep(1)
                if product < 400:
                    con.wait()
#                     等待其他进程
# 这个方法释放底层锁，然后阻塞，直到在另外一个线程中调用同一个条件变量的
# notify() 或 notify_all() 唤醒它，或者直到可选的超时发生。一旦被唤醒或者超时，它重新获得锁并返回。
# if __name__ == '__main__':
#     p = Product(name="p")
#     c = Consumer(name="c")
#     p.start()
#     c.start()




sem = threading.Semaphore(value=2)
# 该类实现信号量对象。信号量对象管理一个原子性的计数器，
# 代表 release() 方法的调用次数减去 acquire() 的调用次数再加上一个初始值。
number = 10
class MySemTread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        sem.acquire()
        global number
        number = number +10
        print(number,threading.current_thread())
        time.sleep(1)
        sem.release()


# 这里就可以看到最多有两个线程在同时运行
# if __name__ == '__main__':
#     for i in range(4):
#         a = MySemTread(name=str(i))
#         a.start()



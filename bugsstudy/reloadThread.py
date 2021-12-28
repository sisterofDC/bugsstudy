import threading
import time



class Mythread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self,name=name)

    def run(self):
        print(threading.current_thread(),self.name)
        time.sleep(1)

#商品
product = 500
#条件变量
con = threading.Condition(threading.Lock())


class Product(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        global product
        while True:
            with con:
                if product < 400:
                    product = product + 50
                    print(product)
                    time.sleep(1)
                    con.notify()


class Consumer(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        global product
        while True:
            with con :
                product = product - 200
                print(product)
                time.sleep(1)
                if product < 400:
                    con.wait()



if __name__ == '__main__':
    p = Product(name="p")
    c = Consumer(name="c")
    p.start()
    c.start()


# join(timeout=None)
# 等待，直到线程终结。这会阻塞调用这个方法的线程，直到被调用 join() 的线程终结 -- 不管是正常终结还是抛出未处理异常 -- 或者直到发生超时，超时选项是可选的。
# 当 timeout 参数存在而且不是 None 时，它应该是一个用于指定操作超时的以秒为单位的浮点数或者分数。因为 join() 总是返回 None ，所以你一定要在 join() 后调用 is_alive() 才能判断是否发生超时 -- 如果线程仍然存活，则 join() 超时。
# 当 timeout 参数不存在或者是 None ，这个操作会阻塞直到线程终结。
# 一个线程可以被 join() 很多次。
# 如果尝试加入当前线程会导致死锁， join() 会引起 RuntimeError 异常。如果尝试 join() 一个尚未开始的线程，也会抛出相同的异常。
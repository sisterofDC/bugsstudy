import threading
import time

# threading的所有知识点
# join 的使用
# 线程的阻塞
# lock  Rlock 可以重载的锁()  信号锁(Semaphore) 事件锁(Event)  条件锁(Condition)
# Queue (线程之间的通信)
# 线程池


# 首先是join
# join(timeout=None)
# 等待，直到线程终结。这会阻塞调用这个方法的线程，直到被调用 join() 的线程终结 -- 不管是正常终结还是抛出未处理异常 -- 或者直到发生超时，超时选项是可选的。
# 当 timeout 参数存在而且不是 None 时，它应该是一个用于指定操作超时的以秒为单位的浮点数或者分数。因为 join() 总是返回 None ，所以你一定要在 join() 后调用 is_alive() 才能判断是否发生超时 -- 如果线程仍然存活，则 join() 超时。
# 当 timeout 参数不存在或者是 None ，这个操作会阻塞直到线程终结。
# 一个线程可以被 join() 很多次。
# 如果尝试加入当前线程会导致死锁， join() 会引起 RuntimeError 异常。如果尝试 join() 一个尚未开始的线程，也会抛出相同的异常。

def test_function(arg):
    time.sleep(1)
    print(threading.current_thread(), str(arg))
    # if __name__ == '__main__':
    # for i in range(10):
    #     t = threading.Thread(target=test_function, args=(i,))
    #     t.start()
    #     t.join()
    #     在线程中添加join可以实现简单的顺序执行

# lock
# 原始锁是一个在锁定时不属于特定线程的同步基元组件。
# 原始锁处于 "锁定" 或者 "非锁定" 两种状态之一。它被创建时为非锁定状态。它有两个基本方法， acquire() 和 release() 。当状态为非锁定时， acquire() 将状态改为 锁定 并立即返回。当状态是锁定时，
# acquire() 将阻塞至其他线程调用 release() 将其改为非锁定状态，然后 acquire() 调用重置其为锁定状态并返回。 release() 只在锁定状态下调用； 它将状态改为非锁定并立即返回。如果尝试释放一个非锁定的锁，则会引发 RuntimeError 异常。
# 当多个线程在 acquire() 等待状态转变为未锁定被阻塞，然后 release() 重置状态为未锁定时，只有一个线程能继续执行；至于哪个等待线程继续执行没有定义，并且会根据实现而不同。
# 所有方法的执行都是原子性的。

number=0
def lock_test_function(name,lock):
    lock.acquire()
    for i in range(5):
        global number
        number = number + 1
        print(number, "当前是",name, threading.current_thread().name)
    print(lock.locked())
    lock.release()

def lock_test_function_two(name,lock):
    lock.acquire()
    for i in range(5):
        global number
        number = number - 1
        print(number,"当前是",name,threading.current_thread().name)
    lock.release()


# if __name__ == '__main__':
#     lock = threading.Lock()
#     for i in range(4):
#         one = threading.Thread(name="one",target=lock_test_function,args=(str(i),lock))
#         two = threading.Thread(name="two",target=lock_test_function_two,args=(str(i),lock))
#         one.start()
#         two.start()
#     print("最后值为"+str(number))

goods = 50
# Rlock 可以重载的锁()
# Condition



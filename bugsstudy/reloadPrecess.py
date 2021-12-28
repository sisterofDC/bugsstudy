import os
from  multiprocessing import Process
from  time import sleep
tem = 0

# 自己实现的Process类
class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess,self).__init__()
        self.name=name
    def run(self):
        global tem
        while True:
            sleep(1)
            tem=tem+1
            print(self.name,os.getpid(),tem,os.getppid())
            if tem > 10:
                break

if __name__ == '__main__':
    i =0
    for i in range(2):
        p =MyProcess(str(i))
        p.start()

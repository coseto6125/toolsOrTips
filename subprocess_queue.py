# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-22 11:14:05
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-22 12:38:28
# @擷取console開啟管道通信

from queue import Queue
from subprocess import Popen,PIPE
from threading import Thread

class shellProcess(Thread):
    def __init__(self,q):
        super(shellProcess,self).__init__()
        self.q=q
        
    def run(self):
        """
        @ 這裡cmd寫要執行的指令就好
        """
        command = "ping 192.168.1.1 -t"
        p = Popen(command, shell=False, stdout=PIPE,encoding='big5')
        for line in iter(p.stdout.readline, b''):
            self.q.put(line)
 
 
if __name__ == "__main__":
    q = Queue()         #創建通信隊列
    p = shellProcess(q) #建立console線程
    p.start()           #啟動線程
    while True:
        if (m:= q.get()): #當收到消息
            print(m)      #do something here

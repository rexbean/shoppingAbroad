import os
import time
import threading

def fun_timer():
    #os.system('scrapy crawl dealNews')
    print('this is a timer')
    global timer
    timer = threading.Timer(3, fun_timer)
    timer.start()


if __name__ == '__main__':
    pid = os.getpid()
    print('the current pid = '+pid)
    timer = threading.Timer(1, fun_timer)
    timer.start()

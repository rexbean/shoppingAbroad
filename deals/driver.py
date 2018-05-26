import os
import threading
import time

def fun_timer():
    os.system('scrapy crawl dealNews')
    global timer
    timer = threading.Timer(1800, fun_timer)
    timer.start()

if __name__ == '__main__':
    pid = os.getpid()
    print('this pid is ' + str(pid))
    timer = threading.Timer(1, fun_timer)
    timer.start()

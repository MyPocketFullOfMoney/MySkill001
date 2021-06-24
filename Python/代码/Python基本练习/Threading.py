import threading
import time

# 新线程执行代码：
def loop():
    print('thread is running...',threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread{} >>> {}'.format(threading.current_thread().name,n))
        time.sleep(1)
    print('thread {} end'.format(threading.current_thread().name))

# 打印主线程
print('thread {} is running...'.format(threading.current_thread().name))

t = threading.Thread(target=loop, name='LoopThread')

t.start()
t.join()

# 主线程结束
print('thread {} end'.format(threading.current_thread().name))
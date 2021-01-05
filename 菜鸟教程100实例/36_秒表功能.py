# 利用Python的time模块实现秒表功能
# 时间：2021/1/5

import time

print("按下回车开始计时，按下Ctrl + c 停止计时。")

while True:
    print("")
    starttime = time.time()
    print("开始")
    try :
        while True :
            print("计时：",round(time.time() - starttime,0),"秒",end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print("结束")
        endtime = time.time()
        print("总共时间为:",round(endtime - starttime,2),'seces')
        break

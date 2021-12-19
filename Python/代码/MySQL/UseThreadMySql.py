import pymysql
from DBUtils.PooledDB import PooledDB
from queue import Queue
import threading
import copy
import time

"""
  思路：
  1、创建MySql的线程连接池
  2、准备需要插入的数据
  3、多线程需要处理的任务
  4、启动多线程

"""
insert_sql = "insert into test_li.user (username,email,password,create_time) values (%s,%s,%s,%s)"
insert_data = ['ming', '123456@qq.com', '123456', '2021-12-19 10:16:18']
db_info = {'host':'127.0.0.1','port':3306,'user':'root','password':'123456','db':'test_li','charset':'utf8'}

def MySqlConnect(db_info):
    # 生成10个连接
    connect_pool = PooledDB(pymysql,maxconnections=10,**db_info)
    return connect_pool


def MakeData(data,begin:int,end:int):
    "生成executemany执行的数据源"
    "最终数据的格式为：[ [[A,B,C,D]...[A,B,C,D]] , [[A1,B2,C3,D3]...[A,B,C,D]] ]"
    "线程任务每次取出1万数据，执行executemany"
    exec_data = []
    result = []
    name = 0
    for i in range(begin,end+1):
        name += 1
        exec_data.append([name,'123456@qq.com', '123456', '2021-12-19 10:16:18'])
        
        # 10000行一组
        if i % 10000 == 0:
            # 每生成一组数据，进行一次深拷贝，然后清空列表exec_data
            line = copy.deepcopy(exec_data)
            result.append(line)
            exec_data.clear()
                
    return result

def InsertData(pool,data):
    "每调用一次插入函数就从数据库连接池中取出一个连接，完成后关闭连接"
    con = pool.connection()
    cur = con.cursor()
    insert_sql = "insert into test_li.user (username,email,password,create_time) values (%s,%s,%s,%s)"
    try:
        cur.executemany(insert_sql,data)
        con.commit()
        #print('执行成功')
    except Exception as e:
        print('SQL执行失败，原因:',e)
    finally:
        cur.close()
        con.close()

def task(exec_fun,pool,data):
    "多线程执行插入操作"
    # 设置最大队列数和线程数
    q = Queue(maxsize=10)

    
    
    
    while data:
        "取出一组数据，交给线程处理。"
        one_data = data.pop()

        t = threading.Thread(target=exec_fun,args=(pool,one_data,))
        # 线程入队
        q.put(t)
        if (q.full() == True) or (len(data)) == 0:
                    thread_list = []
                    while q.empty() == False:
                        t = q.get()
                        thread_list.append(t)
                        t.start()
                    for t in thread_list:
                        t.join()





# 测试代码
pool = MySqlConnect(db_info)

data = MakeData(insert_data,1,100000)

#InsertData(pool,data)

start_time = time.time()

task(InsertData,pool,data)

print('运行时间:',time.time() - start_time)
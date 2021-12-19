import pymysql

from DBUtils.PooledDB import PooledDB

db_info = {'host': '127.0.0.1', 'port': 3306, 'user': 'root',
           'password': '123456', 'db': 'test_li', 'charset': 'utf8'}

test_li_connect = pymysql.connect(**db_info)

insert_data = [['xiaoming', '123456@qq.com', '123456', '2021-12-19 10:16:18'],
               ['daming', '66666666@qq.com', '123456', '2021-12-19 10:16:18']]

insert_sql = "insert into test_li.user (username,email,password,create_time) values (%s,%s,%s,%s)"

# 获取游标
test_li_cursor = test_li_connect.cursor()

# 执行SQL
try:
    test_li_cursor.executemany(insert_sql,insert_data)
    test_li_connect.commit()
except Exception as e:
    print(e)
finally:
    test_li_cursor.close()
    test_li_connect.close()

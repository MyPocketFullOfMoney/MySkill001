'''
利用pymysql模块连接Mysql
时间:2021/2/28
'''

import pymysql

# 打开数据库连接
# 数据库的ip地址，账号，密码，数据库名称
my_db = pymysql.connect(host="localhost",user="root",password="123456",database="data_li")

# 创建一个游标对象
my_cursor = my_db.cursor()

# 先创建表EMPLOYEE
creat_str = '''CREATE TABLE IF NOT EXISTS  EMPLOYEE(
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT
                ) '''

# 使用execute()方法执行SQL
my_cursor.execute(creat_str)

print('表EMPLOYEE是否存在：',my_cursor.execute("SHOW TABLES LIKE 'EMPLOYEE' "))


# 关闭连接
my_db.close